# Getting started

Use this repository to give a skill-capable assistant focused guidance for the Drupal LMS contributed module (`drupal/lms`). Keep skill setup separate from installing Drupal or configuring a product site.

## Obtain and validate the source

Use Git and Python 3.10 or later:

```bash
git clone https://github.com/org-xelius/xel-drupal-lms.git
cd xel-drupal-lms
python3 tools/validate_repository.py
python3 -m unittest discover -s tests -v
```

The validator needs a safe YAML parser. It uses PyYAML when available and otherwise Ruby/Psych. If neither is available, create a local Python environment and install PyYAML:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install 'PyYAML>=6,<7'
python tools/validate_repository.py
```

These checks validate the skill package, documentation links, source registry and inspector behavior. They do not install or test Drupal.

## Install the skill

The complete installable directory is [skills/drupal-lms](../skills/drupal-lms/SKILL.md). It includes the workflow router, references, templates, UI metadata and helper script. Preserve that directory structure; copying only `SKILL.md` loses the supporting material.

Use your assistant's supported skill-installation workflow, selecting `skills/drupal-lms` from this repository. A suitable installation request is:

> Install the drupal-lms skill from https://github.com/org-xelius/xel-drupal-lms, using skills/drupal-lms as the skill directory.

Verify that the assistant reports a successful installation and can locate the bundled references. Cloning the repository or opening its files alone does not establish installation.

Once installed, start with:

> Use $drupal-lms to assess this feature against existing Drupal LMS configuration and ecosystem modules.

## Use the source in a product project

When installation is unavailable or a team wants an explicit project reference, keep a checkout accessible to the assistant. Merge the [project-guidance template](../skills/drupal-lms/assets/project-AGENTS.md) into the product's existing `AGENTS.md`, preserving its commands and conventions.

Add the actual path to this checkout's `skills/drupal-lms/SKILL.md`. For example:

```text
For Drupal LMS work, read /path/to/xel-drupal-lms/skills/drupal-lms/SKILL.md
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
