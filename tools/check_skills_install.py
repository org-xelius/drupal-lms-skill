#!/usr/bin/env python3
"""Check Skills CLI discovery and installation in a temporary Codex project."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLI_VERSION = "1.7.6"
SKILL_NAME = "drupal-lms"


def validate_discovery(output: str) -> None:
    plain = re.sub(r"\x1b\[[0-?]*[ -/]*[@-~]", "", output)
    if not re.search(rf"(?m)^[ \t│]*{re.escape(SKILL_NAME)}[ \t]*$", plain):
        raise ValueError("The Skills CLI did not list drupal-lms")


def bundle_files(root: Path) -> dict[str, bytes]:
    paths = list(root.rglob("*"))
    if root.is_symlink() or any(path.is_symlink() for path in paths):
        raise ValueError("The copy installation contains a symlink")
    return {path.relative_to(root).as_posix(): path.read_bytes() for path in paths if path.is_file()}


def compare_bundles(source: Path, installed: Path) -> int:
    expected, actual = bundle_files(source), bundle_files(installed)
    missing, extra = sorted(expected.keys() - actual.keys()), sorted(actual.keys() - expected.keys())
    changed = sorted(name for name in expected.keys() & actual.keys() if expected[name] != actual[name])
    if missing or extra or changed:
        raise ValueError(f"Installed bundle mismatch: missing={missing}, extra={extra}, changed={changed}")
    return len(expected)


def run_cli(command: list[str], arguments: list[str], project: Path) -> str:
    env = dict(os.environ, DISABLE_TELEMETRY="1")
    result = subprocess.run(
        [*command, *arguments], cwd=project, env=env,
        capture_output=True, text=True, timeout=45,
    )
    if result.returncode:
        detail = (result.stdout + result.stderr)[-4000:]
        raise ValueError(f"Skills CLI failed ({result.returncode}):\n{detail}")
    return result.stdout


def check_installation(cli_file: Path | None) -> dict:
    if cli_file:
        cli_file = cli_file.resolve()
        if not cli_file.is_file():
            raise ValueError("The supplied CLI entry point is not a file")
        command = ["node", str(cli_file)]
        launcher = "existing-cli"
    else:
        command = ["npx", "--yes", f"skills@{CLI_VERSION}"]
        launcher = "npx"

    with tempfile.TemporaryDirectory(prefix="drupal-lms-install-") as temporary:
        temporary_root = Path(temporary)
        source = temporary_root / "source"
        project = temporary_root / "project"
        project.mkdir()
        source_skill = source / "skills" / SKILL_NAME
        shutil.copytree(
            ROOT / "skills" / SKILL_NAME, source_skill,
            ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store"),
        )
        shutil.copy2(ROOT / "skills.sh.json", source / "skills.sh.json")

        version = run_cli(command, ["--version"], project).strip()
        if version != CLI_VERSION:
            raise ValueError(f"Expected Skills CLI {CLI_VERSION}, received {version!r}")
        validate_discovery(run_cli(command, ["add", str(source), "--list"], project))
        run_cli(command, [
            "add", str(source), "--skill", SKILL_NAME,
            "--agent", "codex", "--copy", "--yes",
        ], project)

        installed = project / ".agents" / "skills" / SKILL_NAME
        if not (installed / "SKILL.md").is_file():
            raise ValueError("The Codex project installation is missing SKILL.md")
        file_count = compare_bundles(source_skill, installed)

    return {
        "skill": SKILL_NAME,
        "cli_version": CLI_VERSION,
        "launcher": launcher,
        "discovery_verified": True,
        "codex_project_install_verified": True,
        "bundled_files_verified": file_count,
        "test_telemetry_enabled": False,
        "remote_install_verified": False,
        "skills_sh_listing_verified": False,
        "result": "passed",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cli", type=Path, help="Existing official skills/bin/cli.mjs entry point")
    args = parser.parse_args()
    try:
        result = check_installation(args.cli)
    except (ValueError, OSError, subprocess.SubprocessError) as exc:
        print(f"Installation check failed: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
