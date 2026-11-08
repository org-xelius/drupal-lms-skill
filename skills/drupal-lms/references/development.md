# Product development and integration

## Choose the implementation

Read the ecosystem reference and complete `assets/feature-plan.md` for substantial features. Establish learner, teacher and administrator behavior, then map it to existing configuration/extensions before defining custom code.

Use the existing repository/environment. For a new sandbox, evaluate the [upstream DDEV starter](https://github.com/graber-1/drupal_lms_ddev) recommended by LMS. Inspect its current constraints, configuration and instructions. Its Composer scripts are starter-specific, not universal Drupal commands.

Review [setup](https://www.drupal.org/docs/extending-drupal/contributed-modules/contributed-module-documentation/drupal-lms/course-creators-guide-for-drupal-lms/installation-and-setup). Enabling LMS alone does not supply every necessary Activity Type, Group permission, View and block.

| Requirement | Start here |
|---|---|
| Catalogue, dashboard, progress listing | Views, entity relationships, access and displays |
| Approvals, uploads, certificates, messages, packages, migration | Relevant ecosystem module/configuration |
| Branding, cards, navigation, presentation | Theme templates, libraries, display modes and blocks |
| Cross-system business behavior | Small injected service, supported event/hook or integration |
| Missing learner interaction/scoring | Plugin workflow after the reuse assessment |
| Modal editing or specialized storage | Installed Modal Subform/Field APIs, if necessary |

Inspect relevant service, route, permission, schema and library definitions. Verify event/hook names and parameters. Use dependency injection and existing contracts.

Sources: [services](https://www.drupal.org/docs/extending-drupal/contributed-modules/contributed-module-documentation/drupal-lms/developers-guide-for-drupal-lms/services-managers-hooks-and-query-alters), [forms](https://www.drupal.org/docs/extending-drupal/contributed-modules/contributed-module-documentation/drupal-lms/developers-guide-for-drupal-lms/form-system), [cookbook](https://www.drupal.org/docs/extending-drupal/contributed-modules/contributed-module-documentation/drupal-lms/developers-guide-for-drupal-lms/developers-cookbook).

## Preserve lifecycle and permissions

Use installed TrainingManager APIs for state mutations and handle documented exceptions. Avoid attempt-initializing methods in read-only reports. Specify current/latest/completed/all attempts and prevent duplicate rows from class/group relationships.

Scope reports to authorized accounts/groups. Include outsiders and teachers outside the relevant cohort in access checks when affected.

Identify which form layer owns navigation, submission, evaluation and feedback. Reuse installed modal components; avoid replacing the entire answer form for a small interaction.

## Implement and deploy

Distinguish module defaults, optional configuration and site exports. Adding `config/install` files does not update an already-enabled module; use the project's update mechanism.

Use render arrays, translations, safe text rendering and appropriate cache metadata. Respect AJAX rebuilds and the site's Drupal behavior/once pattern. Preserve focus and accessible feedback. Verify template/library names from source.

Source: [theming/frontend integration](https://www.drupal.org/docs/extending-drupal/contributed-modules/contributed-module-documentation/drupal-lms/developers-guide-for-drupal-lms/theming-and-frontend-integration).

## Verify and troubleshoot

1. Run relevant project checks, including syntax, PHPCS/PHPStan where configured.
2. Use focused unit/kernel coverage for meaningful scoring, storage or service behavior.
3. Use functional/functional JavaScript checks for forms, AJAX, membership and progression.
4. Exercise relevant roles, permissions and attempts in a development environment.
5. Check deployment dependencies and effects on existing learning records.

The official [local QA](https://www.drupal.org/docs/extending-drupal/contributed-modules/contributed-module-documentation/drupal-lms/developers-guide-for-drupal-lms/local-development-qa) and [testing/deployment](https://www.drupal.org/docs/extending-drupal/contributed-modules/contributed-module-documentation/drupal-lms/developers-guide-for-drupal-lms/testing-and-deployment) pages describe starter scripts, YAML fixtures and LMS test helpers. Inspect them before reuse. Keep fixture imports and sample installation in a disposable environment.

Reproduce problems as the affected role. Inspect relevant logs, form errors, requests and configuration. Match exception handling to installed source and the [troubleshooting guide](https://www.drupal.org/docs/extending-drupal/contributed-modules/contributed-module-documentation/drupal-lms/developers-guide-for-drupal-lms/error-handling-troubleshooting).

Report module choices, changed files/configuration, meaningful checks and source/runtime limits. Do not claim a deployment from a local change.
