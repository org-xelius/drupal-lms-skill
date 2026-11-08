"""Regression checks for discovery, copied bundles and portable documentation."""

import tempfile
import unittest
from pathlib import Path

from tools.check_skills_install import compare_bundles, validate_discovery
from tools.validate_repository import check_local_links, validate_directory_config


class DiscoveryTest(unittest.TestCase):
    def test_a_source_path_is_not_a_discovered_skill(self):
        with self.assertRaisesRegex(ValueError, "did not list"):
            validate_discovery("Source: /tmp/drupal-lms-install/source\nNo skills found\n")

    def test_the_cli_skill_row_can_include_terminal_colors(self):
        validate_discovery("│\n│    \x1b[32mdrupal-lms\x1b[0m\n│\n")


class BundleTest(unittest.TestCase):
    def test_missing_extra_and_changed_files_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            source, target = Path(directory) / "source", Path(directory) / "target"
            source.mkdir()
            target.mkdir()
            (source / "SKILL.md").write_bytes(b"skill")
            for case in ("missing", "extra", "changed"):
                with self.subTest(case=case):
                    (target / "SKILL.md").write_bytes(b"changed" if case == "changed" else b"skill")
                    if case == "missing":
                        (target / "SKILL.md").unlink()
                    if case == "extra":
                        (target / "unexpected.py").write_bytes(b"extra")
                    with self.assertRaisesRegex(ValueError, case):
                        compare_bundles(source, target)
                    for path in target.iterdir():
                        path.unlink()

    def test_copied_files_must_not_be_symlinks(self):
        with tempfile.TemporaryDirectory() as directory:
            source, target = Path(directory) / "source", Path(directory) / "target"
            source.mkdir()
            target.mkdir()
            (source / "SKILL.md").write_bytes(b"skill")
            (target / "SKILL.md").symlink_to(source / "SKILL.md")
            with self.assertRaisesRegex(ValueError, "symlink"):
                compare_bundles(source, target)


class DocumentationTest(unittest.TestCase):
    def test_missing_and_escaping_links_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "bundle"
            root.mkdir()
            document = root / "README.md"
            (Path(directory) / "outside.md").write_text("outside")
            for link, reason in (("missing.md", "Broken"), ("../outside.md", "leaves")):
                with self.subTest(link=link):
                    document.write_text(f"[link]({link})")
                    with self.assertRaisesRegex(ValueError, reason):
                        check_local_links([document], root)

    def test_local_and_external_links_can_be_mixed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "usage.md").write_text("# Usage")
            document = root / "README.md"
            document.write_text("[usage](usage.md#usage) [web](https://skills.sh) [heading](#install)")
            self.assertEqual(check_local_links([document], root), 1)

    def test_non_object_directory_configuration_has_a_clear_error(self):
        with self.assertRaisesRegex(ValueError, "must be an object"):
            validate_directory_config([], "drupal-lms")

    def test_non_text_directory_description_is_rejected(self):
        config = {"$schema": "https://skills.sh/schemas/skills.sh.schema.json",
                  "groupings": [{"title": "LMS", "description": [], "skills": ["drupal-lms"]}]}
        with self.assertRaisesRegex(ValueError, "description"):
            validate_directory_config(config, "drupal-lms")


if __name__ == "__main__":
    unittest.main()
