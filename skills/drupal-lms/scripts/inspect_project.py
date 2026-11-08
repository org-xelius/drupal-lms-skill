#!/usr/bin/env python3
"""Inspect Drupal LMS project files without network, database access or writes."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


RELATED_PACKAGES = {
    "drupal/group", "drupal/grequest", "drupal/webform", "drupal/message",
    "drupal/entity_print", "drupal/fillpdf", "drupal/h5p", "drupal/migrate_plus",
}
CONTRACT_FILES = (
    "lms.info.yml", "lms.services.yml", "composer.json",
    "src/Attribute/ActivityAnswer.php",
    "src/Plugin/ActivityAnswerInterface.php",
    "src/Plugin/ActivityAnswerBase.php", "src/ActivityAnswerManager.php",
    "src/TrainingManager.php",
    "modules/lms_answer_plugins/src/Plugin/WithFeedbackPluginTrait.php",
)


def related(name: str) -> bool:
    return name.startswith(("drupal/lms", "drupal/core")) or name in RELATED_PACKAGES


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"Cannot read valid JSON from {path.name}: {exc}") from exc


def read_object(path: Path) -> dict[str, Any]:
    data = read_json(path)
    if not isinstance(data, dict):
        raise ValueError(f"{path.name} must contain a JSON object")
    return data


def package_versions(packages: Any, label: str) -> dict[str, str | None]:
    if not isinstance(packages, list):
        raise ValueError(f"{label} must be an array")
    result = {}
    for package in packages:
        if not isinstance(package, dict) or not isinstance(package.get("name"), str):
            raise ValueError(f"{label} contains an invalid package record")
        if related(package["name"]):
            version = package.get("version")
            result[package["name"]] = version if isinstance(version, str) else None
    return dict(sorted(result.items()))


def child_path(root: Path, value: str) -> Path | None:
    path = (root / value).resolve()
    return path if path.is_relative_to(root) else None


def inspect_project(root: Path) -> dict[str, Any]:
    root = root.resolve()
    if not root.is_dir():
        raise ValueError("Project root must be an existing directory")
    composer_path = root / "composer.json"
    lock_path = root / "composer.lock"
    composer = read_object(composer_path) if composer_path.is_file() else {}
    lock = read_object(lock_path) if lock_path.is_file() else {}
    warnings = []

    declared = {}
    for section in ("require", "require-dev"):
        values = composer.get(section, {})
        if not isinstance(values, dict):
            raise ValueError(f"composer.json {section} must be an object")
        declared[section] = {
            name: version for name, version in sorted(values.items()) if related(name)
        }
    locked = package_versions(lock.get("packages", []), "composer.lock packages")
    locked_dev = package_versions(lock.get("packages-dev", []), "composer.lock packages-dev")

    config = composer.get("config", {})
    if not isinstance(config, dict):
        raise ValueError("composer.json config must be an object")
    vendor = config.get("vendor-dir", "vendor")
    if not isinstance(vendor, str):
        raise ValueError("composer.json vendor-dir must be a string")
    vendor_path = child_path(root, vendor)
    installed_path = vendor_path / "composer/installed.json" if vendor_path else None
    if vendor_path is None:
        warnings.append("External vendor directory was not inspected")
    installed = {}
    if installed_path and installed_path.is_file():
        data = read_json(installed_path)
        if isinstance(data, dict) and "packages" not in data:
            raise ValueError("installed.json must contain a packages array")
        packages = data["packages"] if isinstance(data, dict) else data
        installed = package_versions(packages, "installed-package metadata")

    roots = ["web", "docroot", "."]
    extra = composer.get("extra", {})
    if not isinstance(extra, dict):
        raise ValueError("composer.json extra must be an object")
    scaffold = extra.get("drupal-scaffold", {})
    if isinstance(scaffold, dict):
        locations = scaffold.get("locations", {})
        if isinstance(locations, dict) and isinstance(locations.get("web-root"), str):
            roots.insert(0, locations["web-root"])
    webroots = []
    for value in roots:
        candidate = child_path(root, value)
        if candidate and candidate not in webroots:
            webroots.append(candidate)

    locations = []
    for webroot in webroots:
        for directory in ("modules/contrib/lms", "modules/custom/lms", "modules/lms"):
            module = webroot / directory
            if (module / "lms.info.yml").is_file():
                locations.append({
                    "path": str(module.relative_to(root)),
                    "files_present": {name: (module / name).is_file() for name in CONTRACT_FILES},
                })

    if not composer_path.is_file():
        warnings.append("No composer.json at the supplied root; no parent search was performed")
    if not lock_path.is_file():
        warnings.append("No composer.lock; resolved dependency versions are unknown")
    if not installed_path or not installed_path.is_file():
        warnings.append("No installed.json metadata; installed package versions are unknown")
    if not locations:
        warnings.append("No LMS source found in the inspected module locations")
    return {
        "project_root": str(root),
        "composer_json_present": composer_path.is_file(),
        "composer_lock_present": lock_path.is_file(),
        "declared_constraints": declared,
        "locked_packages": locked,
        "locked_dev_packages": locked_dev,
        "installed_package_metadata_present": bool(installed_path and installed_path.is_file()),
        "installed_packages": installed,
        "lms_source_locations": locations,
        "enabled_modules": "not_checked",
        "runtime_verified": False,
        "database_accessed": False,
        "network_accessed": False,
        "files_modified": False,
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_root", nargs="?", default=".")
    args = parser.parse_args()
    try:
        result = inspect_project(Path(args.project_root))
    except ValueError as exc:
        print(f"Inspection failed: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
