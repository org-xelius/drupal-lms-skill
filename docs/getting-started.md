# Getting started

Use this repository to give a skill-capable assistant focused guidance for the Drupal LMS contributed module (`drupal/lms`). Keep skill setup separate from installing Drupal or configuring a product site.

## Install with npx

With Node.js/npm available, run from your product project:

```bash
npx skills add org-xelius/drupal-lms-skill --skill drupal-lms
```

Select the coding agents when prompted. For a Codex project, use `--agent codex`; add `--global` only when you want a user-level installation across projects. See [distribution](distribution.md) for the complete flow and the tested CLI/Node versions.

## Obtain and validate the source

Use Git and Python 3.10 or later:

```bash
git clone https://github.com/org-xelius/drupal-lms-skill.git
cd drupal-lms-skill
python3 tools/validate_repository.py
python3 -m unittest discover -s tests -v
python3 tools/check_skills_install.py
```

The validator needs a safe YAML parser. It uses PyYAML when available and otherwise Ruby/Psych. If neither is available, create a local Python environment and install PyYAML:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install 'PyYAML>=6,<7'
python tools/validate_repository.py
```

These checks validate the package, documentation links, source registry, inspector and isolated Skills CLI installation. The installation check uses Node.js/npm and a pinned CLI version. They do not install or test Drupal.

## Other installation workflows

The complete installable directory is [skills/drupal-lms](../skills/drupal-lms/SKILL.md). It includes the workflow router, references, templates, UI metadata and helper script. Preserve that directory structure; copying only `SKILL.md` loses the supporting material.

For an assistant that manages its own skill directory rather than a supported local coding agent, use its installation workflow with `skills/drupal-lms`. A suitable request is:

> Install the drupal-lms skill from https://github.com/org-xelius/drupal-lms-skill, using skills/drupal-lms as the skill directory.

Verify installation in the chosen tool and that it can locate bundled references. A Skills CLI installation into a local coding agent does not establish an account-wide ChatGPT skill installation. Cloning the repository or opening its files alone does not establish either.

Once installed, start with:

> Use $drupal-lms to assess this feature against existing Drupal LMS configuration and ecosystem modules.

## Use the source in a product project

When installation is unavailable or a team wants an explicit project reference, keep a checkout accessible to the assistant. Merge the [project-guidance template](../skills/drupal-lms/assets/project-AGENTS.md) into the product's existing `AGENTS.md`, preserving its commands and conventions.

Add the actual path to this checkout's `skills/drupal-lms/SKILL.md`. For example:

```text
For Drupal LMS work, read /path/to/drupal-lms-skill/skills/drupal-lms/SKILL.md
and the workflow references relevant to the request.
```

Keep this as project guidance; it does not imply that the skill is installed for other projects or accounts. Do not commit a teammate's machine-specific absolute path as a shared installation requirement.

## Establish the product baseline

Provide the actual Drupal repository or project root. Run the read-only helper against it:

```bash
python3 skills/drupal-lms/scripts/inspect_project.py /path/to/drupal-project
```

The JSON report distinguishes declared constraints, locked packages, installed-package metadata and discovered LMS source files. It does not access the database, check enabled modules or prove runtime compatibility. It does not read Drupal settings or environment files.

Confirm enabled modules, permissions, membership structure and runtime behavior through the product's established tooling. Use its existing local environment. The [upstream LMS starter](https://github.com/graber-1/drupal_lms_ddev) is a candidate for a new sandbox; this skill repository itself is not that starter.

Continue with [usage](usage.md), [feature planning](product-planning.md) and the [validation record](../VALIDATION.md).
