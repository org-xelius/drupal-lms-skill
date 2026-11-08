---
name: drupal-lms
description: "Create courses and build products using the Drupal LMS contributed module (drupal/lms). Use for Drupal LMS course authoring, lessons, activities, assessment, enrolment, cohorts, progress, reporting, site setup, theming, integrations, troubleshooting, ecosystem module selection, or custom Activity-Answer plugins. Evaluate existing LMS configuration and ecosystem modules before custom code. Apply specifically to drupal/lms, rather than assuming other Drupal LMS products share its APIs."
---

# Drupal LMS

Build a Drupal LMS product through three focused workflows. Select the smallest relevant workflow, reuse existing capabilities, and verify version-sensitive instructions against the project.

## Establish the project context

1. Read the project's applicable `AGENTS.md` and existing implementation before changing files.
2. Identify whether the request concerns course content, product configuration, application code, an Activity-Answer plugin, or a combination.
3. Establish Drupal, PHP, Group and LMS versions, selected extensions, environment and available checks. Run `python3 scripts/inspect_project.py /path/to/project` from this skill when project files are available. Treat lockfile versions as resolved dependencies, installed-package metadata as installation evidence, and neither as proof that a module is enabled.
4. Read [compatibility.md](references/compatibility.md) before recommending constraints, executable commands, service calls or plugin signatures. Continue useful planning with stated assumptions when no Drupal project is available.
5. Read [architecture.md](references/architecture.md) when relationships, membership, progress, revisions or contextual parameters affect the task.

## Choose an existing implementation first

Apply this order to each proposed product feature:

1. Configure Drupal LMS and existing Activity Types, Group roles, Views, blocks or theme.
2. Evaluate the relevant [ecosystem modules](references/ecosystem.md), including dependency chains and actual feature coverage.
3. Consider another suitable Drupal module or a small integration with an existing capability.
4. Add a custom service, plugin or other extension only for a demonstrated remaining gap.

Prefer a small, coherent dependency set. Do not install the entire ecosystem by default, reject a suitable module merely because it is pre-release, or treat a module's name as proof of suitability. Check release compatibility, maintenance, documented limitations and operational needs in proportion to the feature.

For a narrow bug fix, inspect the affected capability and dependencies; avoid repeating a full ecosystem audit without a relevant change.

Record substantial feature decisions in [feature-plan.md](assets/feature-plan.md). Identify the reused capability, selected modules, evidence, remaining gap and learner/teacher acceptance criteria before writing custom code.

## Route the work

| Request | Load | Produce |
|---|---|---|
| Author learning material; configure assessment; manage learners | [course-creation.md](references/course-creation.md) | Course blueprint, activities, configuration or an operational change |
| Build a feature; set up Drupal; change permissions, Views, services or theme; troubleshoot | [development.md](references/development.md) | Module-based decision, implementation and relevant verification |
| Implement a new interaction, scoring model or feedback mechanism | [activity-answer-plugins.md](references/activity-answer-plugins.md) | Gap assessment, plugin contract and version-checked implementation |
| Add approvals, uploads, certificates, messages, content packages, import or migration | [ecosystem.md](references/ecosystem.md) plus the relevant workflow | Configured extension or a justified integration |

Combine workflows when necessary. Keep course authoring in control of the learning objective, use development for platform integration, and use the plugin workflow for a verified interaction gap. Treat Modal Subform and Field plugins as development tasks unless they support the Activity-Answer implementation.

## Apply shared rules

- Distinguish content, configuration and executable code. Do not present an authoring blueprint as an importable course archive or assume configuration export contains course entities.
- Use the project's membership model and permission checks. Verify as the affected learner/teacher; an administrator's successful request is insufficient access evidence.
- Use supported LMS services for progression changes. Do not write directly to status tables or assume a read-looking API has no side effects.
- Check revisions and existing attempts before changing reused activities, grading or navigation.
- Keep contributed modules unmodified for product customizations. Prefer configuration, theme overrides, supported extension points and small custom modules.
- Match signatures and dependencies to installed source. Flag discrepancies with older documentation; do not invent APIs, events, fields, hooks or plugin IDs.
- Preserve Form API validation, access checks, cache metadata, translation and accessible interaction.
- Use non-destructive inspection first. Run reinstall, sample imports, progress resets, migration rollbacks or deletion only within the user's authorized scope and intended environment.

## Verify and report

Scale verification to the change. Check course behavior as learner and teacher; check significant code with the project's standards, analysis and relevant tests. Follow [development.md](references/development.md) for verification.

For feature work, report the requirement, reused capability, dependency chain, remaining customization and acceptance evidence. For code, identify changed files and meaningful checks. Distinguish documentation review, syntax checks, source/API checks and runtime verification. Do not claim installation or a working Drupal feature from generated files alone.

## Use bundled resources

- Copy [course-blueprint.md](assets/course-blueprint.md) for course and activity specifications.
- Copy [feature-plan.md](assets/feature-plan.md) for requirements and module decisions.
- Copy [plugin-contract.md](assets/plugin-contract.md) before implementing an interaction.
- Adapt [project-AGENTS.md](assets/project-AGENTS.md) when adding product guidance; preserve existing instructions.
- Run [inspect_project.py](scripts/inspect_project.py) for a file-based dependency/source inventory without network or database access.
- Use [sources.md](references/sources.md) and [source-index.json](references/source-index.json) for canonical sources, review dates and evidence limits. Refresh affected references after upgrades or discrepancies; no background schedule is implied.
