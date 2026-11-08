# Contributing and maintenance

Keep one short skill router and three focused workflows. Evaluate existing LMS modules before adding custom-code guidance, and retain source/runtime evidence limits.

## Contributor setup

```bash
git clone https://github.com/org-xelius/drupal-lms-skill.git
cd drupal-lms-skill
```

Use Python 3.10+, Node.js 22.20+ and npm. YAML checks use PyYAML or system Ruby/Psych. If neither parser is available:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install 'PyYAML>=6,<7'
```

## Validate

```bash
python3 tools/validate_repository.py
python3 -m unittest discover -s tests -v
python3 tools/check_skills_install.py
git diff --check
```

The validator checks metadata, local file links, source completeness, directory configuration and CI structure. Tests cover dependency evidence, malformed inputs, portable links and installer failures. The installation check uses a temporary project and requires an exact match with every bundled file.

The installation check pins Skills CLI 1.7.6. For offline verification with an existing official copy:

```bash
python3 tools/check_skills_install.py --cli /absolute/path/to/skills/bin/cli.mjs
```

This skips the npx download step. Record that distinction; test telemetry stays disabled. CI uses the normal npx launcher with Node.js 24.

## Update guidance and evidence

Edit routing in `skills/drupal-lms/SKILL.md`, procedures in its `references/`, output templates in `assets/`, and UI metadata in `agents/openai.yaml`. Keep reference links directly reachable from the router.

Refresh the affected canonical sources after dependency changes or discrepancies. Update dates and observations together in `references/source-index.json` and the corresponding guidance. The registry covers three guides, 29 chapters and 11 ecosystem projects; adjust completeness checks when that agreed scope changes.

Review current requirements before changing the CLI pin. For substantial workflow changes, exercise a representative request using the updated skill. Record completed checks in [VALIDATION.md](../VALIDATION.md), with documentation, source and runtime evidence distinguished.

## Repository description

The intended GitHub About text is stored in [.github/description.txt](../.github/description.txt), including the npx command. Committing the file does not update GitHub's live metadata. An authorized maintainer can paste it into the repository's About description or use [GitHub CLI](https://cli.github.com/manual/gh_repo_edit):

```bash
gh repo edit org-xelius/drupal-lms-skill --description "$(cat .github/description.txt)"
```

## Publish

Review and stage the intended source/documentation only. Preserve existing remote history and repository protections; keep credentials, dependencies, caches and local installations out of the repository. Verify remote publication and CI results before reporting them as complete. Installing a selected skill version remains a separate operation.
