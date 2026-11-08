# Drupal LMS skill by Xelius

Create Drupal LMS courses, build product features with existing modules, and develop Activity-Answer plugins with one agent skill.

## Install

```bash
npx skills add org-xelius/drupal-lms-skill --skill drupal-lms
```

Run from your product project with Node.js 22.20+ and npm. Choose your coding agents when prompted. Add `--agent codex` to target Codex, or `--global` for installation across projects. See the [installation guide](docs/distribution.md) for options and authentication.

[![skills.sh installs](https://skills.sh/b/org-xelius/drupal-lms-skill)](https://skills.sh/org-xelius/drupal-lms-skill)

## Use

Ask your agent:

> Use $drupal-lms to plan this feature, evaluate existing modules, and implement the remaining gap.

| Workflow | What it covers |
|---|---|
| [Course creation](skills/drupal-lms/references/course-creation.md) | Lessons, activities, assessment, enrolment and cohorts |
| [Product development](skills/drupal-lms/references/development.md) | Configuration, permissions, Views, theming and integrations |
| [Activity-Answer plugins](skills/drupal-lms/references/activity-answer-plugins.md) | New interactions, scoring and feedback when existing options leave a gap |

The skill checks existing Drupal LMS configuration and ecosystem modules before custom code. It installs agent guidance; configure Drupal LMS in your product project.

## Documentation

- [Getting started](docs/getting-started.md): first task, project inspection and source-based use.
- [Installation and skills.sh](docs/distribution.md): scope, updates, private repositories and directory listing.
- [Workflow examples](docs/usage.md): useful requests and expected outputs.
- [Product planning](docs/product-planning.md): choose modules and define acceptance criteria.
- [Contributing and maintenance](docs/maintenance.md): validation, source updates and repository description.

The [source registry](skills/drupal-lms/references/source-index.json) covers the three official guides and 11 ecosystem projects. See the [validation record](VALIDATION.md) for completed checks and runtime limits.
