# Getting started

Use the skill with the Drupal LMS contributed module (`drupal/lms`).

## Install and verify

Run from your product project:

```bash
npx skills add org-xelius/drupal-lms-skill --skill drupal-lms
npx skills list
```

Select the coding agents when prompted. See [installation options](distribution.md) for scope, authentication and updates. For Codex, the project installation includes `.agents/skills/drupal-lms/SKILL.md` and its supporting files.

## Start a task

Provide your learning material or product requirement and ask:

> Use $drupal-lms to assess this requirement, select existing LMS modules and produce an implementation plan.

For technical work, supply the actual Drupal repository. The skill establishes dependency versions, enabled modules, membership and available checks before version-sensitive implementation. See [workflow examples](usage.md) and the [feature-planning template](../skills/drupal-lms/assets/feature-plan.md).

## Inspect a product project

The optional file-based inspector needs Python 3.10+. From a checkout of this repository:

```bash
python3 skills/drupal-lms/scripts/inspect_project.py /path/to/drupal-project
```

It reports declared, locked and installed-package evidence separately. Enabled modules and runtime behavior require checks in the actual site. The inspector leaves files unchanged and does not read settings, environment files or the database.

## Use the source directly

Keep the complete [skill directory](../skills/drupal-lms/SKILL.md), including its references and assets. Merge the [project-guidance template](../skills/drupal-lms/assets/project-AGENTS.md) into the product's existing `AGENTS.md` and reference the checkout's actual skill path. Preserve existing project conventions.

For assistants with their own skill-management workflow, install that complete directory through the supported mechanism. A local coding-agent installation and an account-wide ChatGPT installation are separate operations.

Contributor setup and package checks are documented in [maintenance](maintenance.md).
