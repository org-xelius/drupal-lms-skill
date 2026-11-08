"""Behavior checks for dependency evidence and read-only inspection."""

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "skills/drupal-lms/scripts/inspect_project.py"
SPEC = importlib.util.spec_from_file_location("inspect_lms_project", SCRIPT)
INSPECTOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(INSPECTOR)


class ProjectInspectionTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def write_json(self, relative, data):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data), encoding="utf-8")

    def test_empty_project_does_not_claim_installation(self):
        result = INSPECTOR.inspect_project(self.root)
        self.assertFalse(result["composer_lock_present"])
        self.assertEqual(result["installed_packages"], {})
        self.assertEqual(result["enabled_modules"], "not_checked")
        self.assertFalse(result["runtime_verified"])

    def test_constraints_locked_and_installed_versions_stay_distinct(self):
        self.write_json("composer.json", {"require": {"drupal/lms": "^1.2", "private/package": "secret-reference"}})
        self.write_json("composer.lock", {"packages": [{"name": "drupal/lms", "version": "1.2.5"}]})
        self.write_json("vendor/composer/installed.json", {"packages": [{"name": "drupal/lms", "version": "1.2.4"}]})
        result = INSPECTOR.inspect_project(self.root)
        self.assertEqual(result["declared_constraints"]["require"]["drupal/lms"], "^1.2")
        self.assertEqual(result["locked_packages"]["drupal/lms"], "1.2.5")
        self.assertEqual(result["installed_packages"]["drupal/lms"], "1.2.4")
        self.assertNotIn("secret-reference", json.dumps(result))
        self.assertEqual(result["enabled_modules"], "not_checked")

    def test_custom_webroot_and_vendor_directory(self):
        self.write_json("composer.json", {
            "config": {"vendor-dir": "build/dependencies"},
            "extra": {"drupal-scaffold": {"locations": {"web-root": "public/"}}},
        })
        self.write_json("build/dependencies/composer/installed.json", [{"name": "drupal/group", "version": "3.3.0"}])
        module = self.root / "public/modules/contrib/lms"
        module.mkdir(parents=True)
        (module / "lms.info.yml").write_text("name: LMS\n")
        result = INSPECTOR.inspect_project(self.root)
        self.assertEqual(result["installed_packages"], {"drupal/group": "3.3.0"})
        self.assertEqual(result["lms_source_locations"][0]["path"], "public/modules/contrib/lms")
        self.assertFalse(result["lms_source_locations"][0]["files_present"]["src/TrainingManager.php"])

    def test_inspection_preserves_files_and_ignores_settings(self):
        self.write_json("composer.json", {"require": {"drupal/lms": "^1.2"}})
        settings = self.root / "settings.php"
        settings.write_text("sensitive-unrelated-value")
        before = {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        result = INSPECTOR.inspect_project(self.root)
        after = {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.assertEqual(before, after)
        self.assertNotIn("sensitive-unrelated-value", json.dumps(result))
        self.assertFalse(result["files_modified"])
        self.assertFalse(result["database_accessed"])

    def test_malformed_metadata_is_an_error_not_an_empty_inventory(self):
        (self.root / "composer.lock").write_text("{broken")
        with self.assertRaisesRegex(ValueError, "valid JSON"):
            INSPECTOR.inspect_project(self.root)

    def test_unexpected_package_shape_is_rejected(self):
        self.write_json("composer.lock", {"packages": {"drupal/lms": "1.2.5"}})
        with self.assertRaisesRegex(ValueError, "must be an array"):
            INSPECTOR.inspect_project(self.root)

    def test_external_vendor_path_is_not_read(self):
        self.write_json("composer.json", {"config": {"vendor-dir": "../outside"}})
        result = INSPECTOR.inspect_project(self.root)
        self.assertFalse(result["installed_package_metadata_present"])
        self.assertIn("External vendor directory was not inspected", result["warnings"])

    def test_command_line_reports_missing_root(self):
        result = subprocess.run([sys.executable, str(SCRIPT), str(self.root / "missing")], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn("existing directory", result.stderr)
        self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()
