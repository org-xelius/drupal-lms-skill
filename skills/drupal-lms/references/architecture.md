# Architecture and product boundaries

Use the official [architecture guide](https://www.drupal.org/docs/extending-drupal/contributed-modules/contributed-module-documentation/drupal-lms/developers-guide-for-drupal-lms/module-architecture) and [entity guide](https://www.drupal.org/docs/extending-drupal/contributed-modules/contributed-module-documentation/drupal-lms/developers-guide-for-drupal-lms/entity-structure). Verify exact names in the installed release.

## Map the learning model

| Concept | Representation | Implementation implication |
|---|---|---|
| Course | Group bundle `lms_course` | Preserve Group access and membership |
| Class/cohort | Group bundle `lms_class`, optional `lms_classes` | Establish direct versus class-based enrolment |
| Lesson | `lms_lesson` content entity | Reuse deliberately across courses |
| Activity | `lms_activity` content entity | Hold the item and instructor-configured fields |
| Activity Type | `lms_activity_type` configuration entity | Select the Activity-Answer plugin |
| Answer | `lms_answer` content entity | Hold the learner response and evaluation |
| Progress | `lms_course_status` / `lms_lesson_status` | Preserve the supported lifecycle |

Follow course to lesson to activity to Activity Type/plugin. Avoid a second course, enrolment or grading model merely for a custom interface.

Check where each setting belongs. Course-to-lesson and lesson-to-activity references can hold contextual parameters, distinct from reusable entity fields. Inspect `LMSReferenceItem` before changing storage or migration mappings.

## Preserve membership and attempts

Establish whether `lms_classes` is enabled. Keep class membership, course access, teacher permissions and reports consistent. Do not assume the first class is the correct enrolment destination. Consult [student management](https://www.drupal.org/docs/extending-drupal/contributed-modules/contributed-module-documentation/drupal-lms/course-creators-guide-for-drupal-lms/student-class-management).

Use the installed `lms.training_manager` for progress changes. The [API guide](https://www.drupal.org/docs/extending-drupal/contributed-modules/contributed-module-documentation/drupal-lms/developers-guide-for-drupal-lms/drupal-lms-api) describes methods that may initialize attempts. Choose reporting read paths that preserve state and enforce access.

## Distinguish change types

| Change | Examples | Delivery |
|---|---|---|
| Content | Courses, lessons, questions, feedback | Authoring or verified content import |
| Configuration | Activity Types, fields, displays, Views, permissions | Drupal configuration for the target site |
| Code | Integrations, new interactions, theme extensions | Custom module/theme using installed APIs |

Evaluate LMS YAML for course portability. Do not substitute configuration synchronization for a content migration.

Read [general settings](https://www.drupal.org/docs/extending-drupal/contributed-modules/contributed-module-documentation/drupal-lms/course-creators-guide-for-drupal-lms/general-settings) before editing live content. Establish revision settings, revisions referenced by attempts and reuse elsewhere. Include an existing attempt in checks when edits affect grading or progression.
