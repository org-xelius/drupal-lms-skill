# Canonical sources and refresh policy

Reviewed: 2026-11-08. Use source-index.json for all 29 linked guide chapters, the 11 ecosystem projects, review scope and release observations. The bundle contains original workflow guidance and summaries, not a full offline mirror. Upstream documentation and code retain their own attribution and licensing.

## Main sources

| Source | Purpose |
|---|---|
| [Drupal LMS](https://www.drupal.org/project/lms) | Product scope, ecosystem and current release |
| [LMS 1.2.5](https://www.drupal.org/project/lms/releases/1.2.5) | Research baseline and version-specific changes |
| [Course Creator's Guide](https://www.drupal.org/docs/extending-drupal/contributed-modules/contributed-module-documentation/drupal-lms/course-creators-guide-for-drupal-lms) | 10 linked chapters |
| [Developer's Guide](https://www.drupal.org/docs/extending-drupal/contributed-modules/contributed-module-documentation/drupal-lms/developers-guide-for-drupal-lms) | 11 linked chapters |
| [Plugin Developer's Guide](https://www.drupal.org/docs/extending-drupal/contributed-modules/contributed-module-documentation/drupal-lms/plugin-developers-guide-for-drupal-lms) | 8 linked chapters |
| [DDEV starter](https://github.com/graber-1/drupal_lms_ddev) | Upstream local-development and QA example |

## Use and refresh

Use the chapter URLs in source-index.json to retrieve the relevant source on demand. Compare installed code with documentation before executable/API changes. Treat roadmap entries as plans until a current release/project source establishes availability.

Refresh relevant guide excerpts and module/release metadata when adopting the skill into a project, changing a dependency or encountering a discrepancy. Update the review date and observations together; keep historical snapshots visibly dated. Do not silently convert research observations into supported-version promises.

## Evidence limits

Official documentation/project excerpts were inspected and indexed; retrieved pages may be cached. A release-page check refreshed LMS Messages to 1.1.0-alpha3 and established the Certificate Entity 1.0.x-dev candidate. The linked membership-request issue is fixed in Group Membership Request 3.2.4. Source-host requests for the 1.2.5 code were unavailable. No Drupal application, enabled-module inventory or live learner flow was available during authoring. Resolve exact APIs and runtime compatibility in the product project.

Documentation can contain inconsistencies. For example, the method guide describes an answering-form requirement while the existing-plugin reference explains inherited no-answer defaults. Inspect the installed interface/base rather than repeating either statement as an absolute rule.

Use source URLs in user-facing technical explanations when precise attribution matters. Do not expose temporary download credentials, local account configuration or unrelated project material.
