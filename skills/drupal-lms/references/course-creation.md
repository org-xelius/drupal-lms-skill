# Course creation and operations

Use this workflow for learning design, authoring, assessment and learner management. Read the ecosystem reference when a requirement needs an extension.

## Design the course

Capture audience, entry knowledge, outcomes, source material, delivery constraints and evidence of success. Distinguish missing instructional material from platform limitations.

Copy `assets/course-blueprint.md`. Map outcomes to lessons, activities and observable assessment. Specify learner actions, expected responses, feedback, grading and completion rules.

## Choose activities

| Need | Existing candidate | Authoring decision |
|---|---|---|
| Read/view information | `no_answer` | Supply content and a transition |
| Instructor-reviewed reflection | `free_text` | Supply a rubric and evaluation procedure |
| Phrase-based practice feedback | `free_text_feedback` | Explain phrase-matching limits; do not promise semantic grading |
| Single/multiple selection | `select` | Configure selection mode at the Activity Type level |
| Selection with practice feedback | `select_feedback` | Define feedback and final-submission expectations |
| Binary question | `true_false` | Write an unambiguous statement |
| Binary question with feedback | `true_false_feedback` | Explain the reasoning |

Confirm registered plugins and configured Activity Types. One plugin may power multiple types. Consult [activity types](https://www.drupal.org/docs/extending-drupal/contributed-modules/contributed-module-documentation/drupal-lms/course-creators-guide-for-drupal-lms/activity-types-and-plugins).

Check ecosystem candidates for uploads, Webform, H5P and content packages before custom interactions. Specify package compatibility, completion and scoring requirements.

## Assemble and configure

1. Confirm Activity Types and authoring permissions.
2. Create/reference activities with prompts, answers, feedback and media.
3. Assemble lessons with intentional ordering, randomization and backward navigation.
4. Add lessons to the course and configure contextual requirements, such as mandatory status, pass threshold, time limit and retry behavior where supported.
5. Decide course navigation and revisit behavior, including access while manual grading is pending.
6. Establish direct or class-based membership and the enrolment path.

Use documented paths as starting points: activities `/admin/lms/activity`, lessons `/admin/lms/lesson`, Activity Types `/admin/lms/activity_type`. Verify course administration paths, labels and available options against the installed release/theme.

Sources: [activities](https://www.drupal.org/docs/extending-drupal/contributed-modules/contributed-module-documentation/drupal-lms/course-creators-guide-for-drupal-lms/activities), [lessons](https://www.drupal.org/docs/extending-drupal/contributed-modules/contributed-module-documentation/drupal-lms/course-creators-guide-for-drupal-lms/lessons), [courses](https://www.drupal.org/docs/extending-drupal/contributed-modules/contributed-module-documentation/drupal-lms/course-creators-guide-for-drupal-lms/courses).

## Manage learning operations

Choose immediate self-enrolment, approval-based requests or staff-managed enrolment. For approval, evaluate LMS Membership Request and its dependency; prevent unrestricted join permissions from bypassing the intended flow.

Use optional classes for cohorts. Confirm which management/reporting screens depend on `lms_classes`. Identify the grading owner and how learners learn evaluation is complete.

Use existing student/result views first. For custom reports, define population, attempts, statuses and access. Check export support separately; a report display does not automatically provide CSV/Excel export.

Sources: [student management](https://www.drupal.org/docs/extending-drupal/contributed-modules/contributed-module-documentation/drupal-lms/course-creators-guide-for-drupal-lms/student-class-management), [reporting](https://www.drupal.org/docs/extending-drupal/contributed-modules/contributed-module-documentation/drupal-lms/course-creators-guide-for-drupal-lms/reporting-and-tracking).

## Deliver and verify

Produce a blueprint or perform authorized site authoring. Generate import packages only after checking the installed importer, schema, dependencies and media handling. Never label the blueprint as an importable archive.

Check enrolment, access denial, navigation, correct/incorrect responses, pending evaluation, pass/fail and completion as relevant learner/teacher accounts. Include an existing attempt for revised/reused content. Check mobile usability, keyboard operation and media against delivery constraints.

Report content gaps and unverified behavior. Distinguish blueprint completion, site authoring and successful course import.
