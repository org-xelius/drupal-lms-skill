# Planning Drupal LMS product features

Turn each requirement into observable learner, teacher and administrator behavior. Then choose the smallest implementation that meets it.

## Follow the reuse order

1. Check the site's existing LMS configuration, Activity Types, Group roles, Views, blocks and theme.
2. Evaluate the relevant ecosystem module and its dependency chain.
3. Consider another suitable Drupal module or a small integration.
4. Use custom code for the remaining demonstrated gap.

Do not install every ecosystem module by default. Check actual capabilities, dependencies and operations rather than treating the project name as proof of suitability.

## Map requirements to candidates

| Requirement | Existing ecosystem candidate |
|---|---|
| Approval before course membership | LMS Membership Request, with Group Membership Request |
| Learner document/file submission | LMS File Upload |
| Structured form activity | LMS Webform, with Webform |
| Course certificates using PDF forms | LMS Certificate and its FillPDF integration |
| Drupal-managed certificate entities/templates | LMS Certificate Entity, with LMS Certificate and Entity Print for PDF output |
| Learning-event messages | LMS Messages, with Message |
| Course import/export packages | LMS YAML |
| xAPI content and learning records | LMS Xapi |
| H5P learning activities | LMS H5P, with H5P and LMS Xapi |
| SCORM content packages | LMS Scorm |
| Opigno migration | LMS Migrate |

Read the [ecosystem reference](../skills/drupal-lms/references/ecosystem.md) for primary sources, dependency choices and dated release observations. Verify the selected release's Composer requirements and enabled modules in the product environment.

## Make the important choices explicit

For certificates, choose the appropriate rendering path. LMS Certificate Entity still requires LMS Certificate; its local PDF route also needs Entity Print and a configured renderer. Do not assume both rendering approaches are necessary.

For H5P, include the LMS Xapi/LRS configuration and test the actual H5P content library's scoring, completion and resume behavior. A working content display does not by itself prove correct LMS progression.

For enrolment and messaging, verify that approval grants the correct course/class membership and that the intended notification follows a successful transition. Review current dependency fixes before applying historical patches.

For portability, distinguish site configuration from course content. Verify the installed LMS YAML format, referenced media and repeated-import behavior. Keep production attempts and enrolments outside course-promotion packages unless an explicitly scoped migration requires them.

## Record the implementation decision

Copy the [feature-plan template](../skills/drupal-lms/assets/feature-plan.md). Record:

- The required user behavior and affected learning records.
- Existing configuration and candidate modules evaluated.
- Selected releases, dependency evidence and operational requirements.
- The uncovered behavior and why custom code is needed, if any.
- Separate configuration, content and code changes.
- Acceptance checks for the relevant roles, attempts and revisions.

Describe material stability, maintenance and advisory-coverage considerations for the selected dependency. Keep dated snapshots as research context, not permanent version pins or blanket reasons to reject existing modules.

## Verify the feature end to end

Test the complete selected integration in a representative course attempt. Include unauthorized access, pending grading, pass/fail and retries where the feature depends on them. Check active attempts during content or grading changes.

Record observed results, not only planned checks. Use the [evidence distinctions](usage.md#read-the-completion-report) when reporting completion.
