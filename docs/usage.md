# Using the three workflows

Use one skill and load only the references relevant to the task. For requests spanning learning design and technical work, combine workflows while keeping the learning objective and acceptance behavior explicit.

## Select the workflow

| Need | Workflow | Expected result |
|---|---|---|
| Structure learning material and assessments | [Course creation](../skills/drupal-lms/references/course-creation.md) | Course/lesson/activity blueprint or authorized site authoring |
| Build a product feature, configure a site or troubleshoot | [Development](../skills/drupal-lms/references/development.md) | Existing-module decision, implementation and relevant verification |
| Add a learning interaction or evaluation behavior | [Activity-Answer plugins](../skills/drupal-lms/references/activity-answer-plugins.md) | Reuse assessment, plugin contract and source-checked implementation if needed |

The skill applies specifically to `drupal/lms`. Do not assume Opigno, Anu LMS or another learning platform uses the same entities, routes or plugin contracts.

## Course creation

Supply the audience, source material, learning outcomes, delivery constraints and desired completion evidence. Add the grading owner and enrolment/cohort requirements when known.

Example request:

> Use $drupal-lms to turn this three-unit staff-training outline into lessons and activities. Include automatically scored questions, a teacher-assessed reflection and an evidence upload. Identify the required existing modules and completion rules.

Use the [course blueprint](../skills/drupal-lms/assets/course-blueprint.md) to capture outcomes, activities, prompts, feedback, grading, navigation and operations. Review proposed instructional assumptions before authoring. Ask the assistant to state whether it delivered a blueprint, changed a site or successfully imported content.

A blueprint is not an importable archive. Course import needs an actual importer and a verified package format.

## Product development

Supply the product repository, affected roles, required behavior, known dependencies and available environment. Keep requests observable: describe who does what and what should happen next.

Example request:

> Use $drupal-lms to plan course-enrolment approval, confirmation messages and locally rendered PDF certificates. Inspect the project first, reuse ecosystem modules and identify any remaining integration work.

Expect a [feature plan](../skills/drupal-lms/assets/feature-plan.md) that separates configuration, content and code. It should identify dependencies, source evidence, the remaining gap and learner/teacher acceptance criteria.

For troubleshooting, supply the failing behavior and affected role. A learner access problem may involve Group membership or class configuration; successful administrator access is not enough to establish that it is fixed.

## Plugin development

Describe the interaction, response data, scoring, feedback and retry/final-submission behavior. Ask for an assessment of existing plugins and ecosystem options before custom PHP.

Example request:

> Use $drupal-lms to assess a five-step ordering activity with partial credit and practice feedback. Evaluate existing content/modules, then define an Activity-Answer implementation only if they leave a gap.

Use the [plugin contract](../skills/drupal-lms/assets/plugin-contract.md). A custom implementation must match the installed attribute, interface, base class, configuration loader and relevant existing plugin. Without source access, expect a documented contract and verification steps rather than certified executable signatures.

## Read the completion report

| Evidence | What it establishes |
|---|---|
| Documentation checked | The proposed behavior is supported by the cited material |
| Dependencies resolved | Composer can select the requested dependency graph |
| Source/API checked | The implementation matches inspected project interfaces and definitions |
| Syntax/analysis checked | Relevant code passes the stated static checks |
| Runtime verified | The stated learner/teacher behavior was exercised in the specified environment |

Keep those claims distinct. A generated file, installed package or discoverable plugin alone does not establish a working learner flow.

See [product planning](product-planning.md) for module decisions and [maintenance](maintenance.md) for updates.
