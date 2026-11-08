# Xelius Drupal LMS skill

Use one skill for course creation, application development and Activity-Answer plugin development with the Drupal LMS contributed module (`drupal/lms`).

Select existing LMS configuration and ecosystem modules before custom code. The bundle maps approval-based enrolment, uploads, Webform, certificates, messages, course portability, xAPI, H5P, SCORM and Opigno migration to their existing projects.

Repository: [org-xelius/xel-drupal-lms](https://github.com/org-xelius/xel-drupal-lms).

This repository contains an assistant skill and its supporting documentation. It does not contain a Drupal site, install the LMS module, or establish a working product environment.

## Documentation

| Guide | Read it for |
|---|---|
| [Getting started](docs/getting-started.md) | Clone, validate, install or use the source in a project |
| [Using the workflows](docs/usage.md) | Course creation, product development, plugins and example requests |
| [Planning product features](docs/product-planning.md) | Choose existing configuration/modules and define the remaining work |
| [Maintenance](docs/maintenance.md) | Update sources, validate changes, interpret CI and record evidence |
| [Validation record](VALIDATION.md) | Completed checks and remaining source/runtime limits |

## Use

The portable skill directory is [skills/drupal-lms](skills/drupal-lms/SKILL.md). Install that complete directory through your assistant's supported skill-installation workflow. Cloning this repository by itself does not install or activate the skill.

After installation, use requests such as:

- `Use $drupal-lms to turn this course outline into lessons, activities and assessments.`
- `Use $drupal-lms to plan enrolment approvals and certificates using existing modules.`
- `Use $drupal-lms to evaluate whether this interaction needs a custom Activity-Answer plugin.`

For project use without installation, follow the [source-based setup](docs/getting-started.md#use-the-source-in-a-product-project). Do not describe project-local source availability as an account-wide skill installation.

## Contents

| Path | Purpose |
|---|---|
| `skills/drupal-lms/SKILL.md` | Short router, shared rules and module-first decisions |
| `skills/drupal-lms/references/` | Three workflows, architecture, compatibility, ecosystem and canonical sources |
| `skills/drupal-lms/assets/` | Course, feature, plugin and project-guidance templates |
| `skills/drupal-lms/scripts/inspect_project.py` | Read-only Composer/source inventory |
| `tools/validate_repository.py` | Metadata, YAML, local links and source-registry validation |
| `tests/` | Behavior checks for the project inspector |

## Validate

Use Python 3.10 or later. YAML validation uses PyYAML if available, otherwise system Ruby/Psych. The skill's project-inspection helper itself uses only the Python standard library.

```bash
python3 tools/validate_repository.py
python3 -m unittest discover -s tests -v
python3 skills/drupal-lms/scripts/inspect_project.py /path/to/drupal-project
```

The GitHub workflow uses Python 3.12 and PyYAML. Checks do not install Drupal or certify extension compatibility.

## Evidence and maintenance

The [source registry](skills/drupal-lms/references/source-index.json) indexes all 29 linked chapters from the three official guides and 11 ecosystem projects. Research observations are dated 2026-11-08 and may come from cached page retrievals; recheck current releases and installed source before implementation.

Exact LMS source signatures and live Drupal behavior were not verified during initial creation. The skill requires those checks in the product environment. It does not ship an invented course-import schema or an unverified executable plugin scaffold.

See [sources](skills/drupal-lms/references/sources.md) for attribution and canonical documentation. Upstream documentation and code retain their respective attribution and licensing; this repository does not contain the upstream source tree.
