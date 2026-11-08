#!/usr/bin/env python3
"""Validate skill metadata, documentation links and the source registry."""

from __future__ import annotations

import ast
import datetime
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/drupal-lms"
INSTALL_COMMAND = "npx skills add org-xelius/drupal-lms-skill --skill drupal-lms"
MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
EXPECTED_MODULES = {
    "lms_membership_request", "lms_file_upload", "lms_webform", "lms_certificate",
    "lms_certificate_entity", "lms_messages", "lms_yaml", "lms_xapi", "lms_h5p",
    "lms_scorm", "lms_migrate",
}


def load_yaml(content: str):
    """Use a real safe YAML parser: PyYAML or system Ruby's Psych."""
    try:
        import yaml
    except ImportError:
        ruby = shutil.which("ruby")
        if not ruby:
            raise ValueError("Install PyYAML or make Ruby/Psych available for YAML validation")
        command = [ruby, "--disable=gems", "-ryaml", "-rjson", "-e",
                   "print JSON.generate(YAML.safe_load(STDIN.read))"]
        result = subprocess.run(command, input=content, text=True, capture_output=True, timeout=20)
        if result.returncode:
            raise ValueError(f"YAML parsing failed: {result.stderr.strip()}")
        return json.loads(result.stdout)
    try:
        return yaml.safe_load(content)
    except yaml.YAMLError as exc:
        raise ValueError(f"YAML parsing failed: {exc}") from exc


def require(condition: bool, message: str):
    if not condition:
        raise ValueError(message)


def check_local_links(documents, boundary: Path) -> int:
    boundary = boundary.resolve()
    count = 0
    for path in documents:
        for target in MARKDOWN_LINK.findall(path.read_text(encoding="utf-8")):
            if re.match(r"[A-Za-z][A-Za-z0-9+.-]*:", target) or target.startswith("#"):
                continue
            resolved = (path.parent / target.split("#", 1)[0]).resolve()
            require(resolved.is_relative_to(boundary), f"Local link leaves its bundle: {path.name}: {target}")
            require(resolved.is_file(), f"Broken local link: {path.name}: {target}")
            count += 1
    return count


def validate_directory_config(config, skill_name: str) -> None:
    require(isinstance(config, dict), "skills.sh configuration must be an object")
    require(config.get("$schema") == "https://skills.sh/schemas/skills.sh.schema.json", "Unexpected skills.sh schema")
    require(set(config) <= {"$schema", "schema", "notGrouped", "groupings", "paths"}, "Unknown skills.sh field")
    require(config.get("notGrouped", "bottom") in ("top", "bottom"), "Invalid ungrouped-skill placement")
    groups = config.get("groupings", [])
    require(isinstance(groups, list) and bool(groups), "Missing skills.sh grouping")
    grouped_skills = []
    for group in groups:
        require(isinstance(group, dict), "Directory group must be an object")
        require(set(group) <= {"title", "description", "skills"}, "Unknown directory group field")
        require(isinstance(group.get("title"), str) and 0 < len(group["title"]) <= 120, "Invalid directory group title")
        description = group.get("description", "")
        require(isinstance(description, str) and len(description) <= 500, "Invalid directory group description")
        names = group.get("skills", [])
        require(isinstance(names, list) and bool(names), "Directory group needs skill names")
        require(all(name == skill_name for name in names), "Directory group refers to an unknown skill")
        grouped_skills.extend(names)
    require(skill_name in grouped_skills, "Directory metadata omits the skill")


def validate() -> dict:
    skill_file = SKILL / "SKILL.md"
    text = skill_file.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    require(match is not None, "SKILL.md needs YAML frontmatter")
    front = load_yaml(match.group(1))
    require(isinstance(front, dict), "Frontmatter must be a mapping")
    require(set(front) == {"name", "description"}, "Use only name and description in frontmatter")
    require(front["name"] == "drupal-lms", "Skill name must match its portable directory")
    description = front["description"]
    require(isinstance(description, str) and 0 < len(description) <= 1024, "Description must be 1-1024 characters")
    require(not any(c in description for c in "<>"), "Description contains angle brackets")
    require(len(text.splitlines()) < 500, "Keep the skill router under 500 lines")
    require("TODO" not in text, "Remove initializer placeholders")

    metadata = load_yaml((SKILL / "agents/openai.yaml").read_text(encoding="utf-8"))
    require(isinstance(metadata, dict), "Agent metadata must be a mapping")
    interface = metadata.get("interface", {})
    require(isinstance(interface, dict), "Agent interface must be a mapping")
    require(isinstance(interface.get("display_name"), str), "Missing display name")
    require(isinstance(interface.get("short_description"), str), "UI description must be text")
    require(isinstance(interface.get("default_prompt"), str), "Default prompt must be text")
    require(25 <= len(interface.get("short_description", "")) <= 64, "UI description length must be 25-64")
    require("$drupal-lms" in interface.get("default_prompt", ""), "Default prompt must mention $drupal-lms")

    skill_documents = sorted(SKILL.rglob("*.md"))
    for path in skill_documents:
        content = path.read_text(encoding="utf-8")
        if len(content.splitlines()) > 100:
            require("## Contents" in content, f"Long reference needs contents: {path.name}")
    references = check_local_links(skill_documents, SKILL)
    direct_links = set(MARKDOWN_LINK.findall(text))
    for path in (SKILL / "references").iterdir():
        require(f"references/{path.name}" in direct_links, f"Reference is not linked from router: {path.name}")

    documents = [ROOT / "README.md", ROOT / "VALIDATION.md", ROOT / "AGENTS.md",
                 *sorted((ROOT / "docs").rglob("*.md"))]
    repository_links = check_local_links(documents, ROOT)
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    first_command = re.search(r"```bash\n(.*?)\n```", readme, re.S)
    require(first_command is not None and first_command.group(1).strip() == INSTALL_COMMAND, "README must lead with the npx install command")
    description = (ROOT / ".github/description.txt").read_text(encoding="utf-8").strip()
    require(bool(description) and len(description) <= 350 and "\n" not in description, "Keep the repository description on one short line")
    require(INSTALL_COMMAND in description, "Repository description must include the install command")

    registry = json.loads((SKILL / "references/source-index.json").read_text(encoding="utf-8"))
    require(registry["schema_version"] == 1, "Unexpected source registry schema")
    datetime.date.fromisoformat(registry["review_date"])
    modules = registry["ecosystem"]
    ids = [module["project_id"] for module in modules]
    require(len(set(ids)) == len(ids), "Duplicate ecosystem project")
    require(set(ids) == EXPECTED_MODULES, "Ecosystem map does not cover the requested projects")
    for module in modules:
        require(module["project_url"] == "https://www.drupal.org/project/" + module["project_id"], "Invalid project URL")
        require(bool(module["documented_supporting_components"]), "Missing dependency review context")
        datetime.date.fromisoformat(module["review_date"])
    guides = registry["guides"]
    require(len(guides) == 3, "Expected the three official guide trees")
    chapters = [chapter for guide in guides for chapter in guide["pages"]]
    require(len(chapters) == 29, "Expected 29 indexed guide chapters")
    require(len({chapter["url"] for chapter in chapters}) == len(chapters), "Duplicate guide chapter")
    require(all(chapter["url"].startswith("https://www.drupal.org/docs/") for chapter in chapters), "Use canonical guide sources")
    for key, value in registry["validation_limits"].items():
        require(isinstance(value, bool), f"Evidence flag must be boolean: {key}")

    validate_directory_config(json.loads((ROOT / "skills.sh.json").read_text(encoding="utf-8")), front["name"])

    workflow = load_yaml((ROOT / ".github/workflows/validate.yml").read_text(encoding="utf-8"))
    require(isinstance(workflow, dict), "CI workflow must be a YAML mapping")
    # YAML 1.1 parsers can interpret the unquoted GitHub key 'on' as True.
    triggers = workflow.get("on", workflow.get(True, workflow.get("true", {})))
    require(isinstance(triggers, dict) and {"push", "pull_request"} <= set(triggers), "Missing CI triggers")
    require(workflow.get("permissions", {}).get("contents") == "read", "CI should require read-only repository access")
    steps = workflow.get("jobs", {}).get("validate", {}).get("steps", [])
    require(any("tools/validate_repository.py" in step.get("run", "") for step in steps), "CI does not validate the bundle")
    require(any("unittest discover" in step.get("run", "") for step in steps), "CI does not run inspector checks")
    require(any(step.get("uses", "").startswith("actions/setup-node@") for step in steps), "CI needs Node for Skills CLI")
    require(any("check_skills_install.py" in step.get("run", "") for step in steps), "CI does not check Skills installation")

    python_files = [*SKILL.rglob("*.py"), *ROOT.glob("tools/*.py"), *ROOT.glob("tests/*.py")]
    for path in python_files:
        ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    return {
        "skill": front["name"], "router_lines": len(text.splitlines()),
        "local_links_checked": references, "guide_chapters": len(chapters),
        "repository_documentation_links_checked": repository_links,
        "ecosystem_projects": len(modules), "python_files_checked": len(python_files),
        "ci_workflow_checked": True, "skills_sh_config_checked": True, "result": "passed",
    }


def main() -> int:
    try:
        result = validate()
    except (ValueError, OSError, KeyError, TypeError, SyntaxError, subprocess.SubprocessError) as exc:
        print(f"Validation failed: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
