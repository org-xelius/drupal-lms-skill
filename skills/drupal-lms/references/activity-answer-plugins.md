# Activity-Answer plugin development

## Establish the gap

Check existing Activity Types and ecosystem candidates first. Uploads, forms, H5P, SCORM and xAPI already have implementation candidates. Prefer configuration or a small extension when suitable.

Copy `assets/plugin-contract.md`. Specify instructor configuration, learner interaction, response data, validation, scoring/evaluation, feedback, retries and reporting. Explain the uncovered need. Prefer standard fields unless storage requirements justify custom types.

Source: [introduction](https://www.drupal.org/docs/extending-drupal/contributed-modules/contributed-module-documentation/drupal-lms/plugin-developers-guide-for-drupal-lms/introduction).

## Verify the installed contract

Inspect paths relative to the installed LMS module:

- `src/Attribute/ActivityAnswer.php`
- `src/Plugin/ActivityAnswerInterface.php`
- `src/Plugin/ActivityAnswerBase.php`
- `src/ActivityAnswerManager.php`
- The closest plugin in `modules/lms_answer_plugins/src/Plugin/ActivityAnswer/`
- `modules/lms_answer_plugins/src/Plugin/WithFeedbackPluginTrait.php` if needed

Locate additional interfaces through source search. For per-lesson activity parameters, investigate the `ActivityParametersInterface` capability mentioned in the LMS 1.2.5 notes.

The documentation describes PHP attribute discovery and classes under `src/Plugin/ActivityAnswer/`, implementing the interface or extending the base. Confirm attribute arguments and signatures before generating PHP. Declare the provider's LMS dependency and `lms_answer_plugins` if its code is used.

Sources: [fundamentals](https://www.drupal.org/docs/extending-drupal/contributed-modules/contributed-module-documentation/drupal-lms/plugin-developers-guide-for-drupal-lms/fundamentals-of-activity-answer-plugins), [integration](https://www.drupal.org/docs/extending-drupal/contributed-modules/contributed-module-documentation/drupal-lms/plugin-developers-guide-for-drupal-lms/integration-and-deployment).

## Design the answer lifecycle

| Concern | Documented extension point | Decision |
|---|---|---|
| Learner form | `answeringForm()` | Preserve defaults/submitted state and server validation |
| Evaluation timing | `evaluatedOnSave()` | Automatic evaluation or teacher review |
| Automatic score | `getScore()` | Verify normalized score, inherited behavior and scaling |
| Teacher display | `evaluationDisplay()` | Safely show the evidence for manual evaluation |
| Practice feedback | Installed trait or supported AJAX | Separate feedback from final submission/state |

Treat this as a documentation map, not an interface declaration. Verify inherited defaults as well as method descriptions. Check empty, invalid, zero/full/partial-score and revisit cases as applicable.

Use the installed Answer API for responses and activity fields for instructor-configured content. Avoid parallel answer tables and browser-authoritative scores.

Source: [methods](https://www.drupal.org/docs/extending-drupal/contributed-modules/contributed-module-documentation/drupal-lms/plugin-developers-guide-for-drupal-lms/required-and-optional-methods).

## Package fields and displays

Use the documented `config/activity_answer/PLUGIN_ID/` location for configuration supplied when an Activity Type selects the plugin. Verify the manager's loading behavior.

Use `_bundle_placeholder_` in applicable activity configuration. Distinguish shared storage from bundle-specific instances and displays. Prototype and export fields in development to avoid guessing schemas. Adapt exports according to the installed loader's requirements.

Test two Activity Types using the same plugin. Check existing storage, dependencies, displays and updates to already-created types. Do not assume template changes retrofit existing Activity Types.

Source: [configuration](https://www.drupal.org/docs/extending-drupal/contributed-modules/contributed-module-documentation/drupal-lms/plugin-developers-guide-for-drupal-lms/plugin-configuration-files).

## Add specialized interaction when necessary

Prefer the installed `WithFeedbackPluginTrait` for supported check-answer feedback. Verify its helper and required methods against a same-release plugin. Add custom AJAX only for the remaining behavior; preserve validation, state and accessible feedback.

Prefer standard fields/widgets. If specialized storage is required, design schema, constraints, widget and display together against the target core version.

Sources: [AJAX](https://www.drupal.org/docs/extending-drupal/contributed-modules/contributed-module-documentation/drupal-lms/plugin-developers-guide-for-drupal-lms/ajax-implementation), [fields/widgets](https://www.drupal.org/docs/extending-drupal/contributed-modules/contributed-module-documentation/drupal-lms/plugin-developers-guide-for-drupal-lms/custom-field-types-and-widgets).

## Complete and verify

Implement discovery, Activity Type configuration, response persistence, evaluation and then optional feedback. Check [existing plugins](https://www.drupal.org/docs/extending-drupal/contributed-modules/contributed-module-documentation/drupal-lms/plugin-developers-guide-for-drupal-lms/reference-existing-plugins) against installed source before reuse.

Validate discovery, configuration installation, scoring/manual evaluation, persistence, access, feedback/rebuilds and course/lesson completion. Include a real attempt: discovery alone does not establish a working plugin.

Deliver the provider module, configuration, meaningful checks and usage instructions. If source/runtime access is absent, deliver the contract and documented plan with that limit stated.
