# Drupal LMS product guidance

Merge these instructions with the product's existing guidance; retain its commands and conventions.

- Use the `drupal-lms` skill for this product's Drupal LMS work. Load the relevant course, development or Activity-Answer workflow.
- Inspect the project's actual Drupal, PHP, Group, LMS and extension versions before version-sensitive implementation.
- Choose existing LMS configuration first, then relevant ecosystem/Drupal modules, then a small integration or justified custom extension.
- Record feature/module choices, dependency chains, remaining gaps and acceptance evidence.
- Keep course content, Drupal configuration and custom code distinct.
- Preserve membership/access, attempts, grading and revision behavior.
- Use installed extension points and learning-state APIs; avoid direct progression-table updates and product customizations inside contributed modules.
- Verify behavior as the affected learner/teacher and report source/runtime limits.

## Project facts to establish

- Repository, Drupal root and local execution commands:
- Locked/installed/enabled dependency versions:
- Direct membership or class/cohort structure:
- Selected modules and configuration/deployment process:
- Relevant coding standards, analysis and tests:

Do not treat unresolved entries as established project facts.
