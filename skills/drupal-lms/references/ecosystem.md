# Build with the LMS ecosystem

## Contents

- Selection workflow
- Feature-to-module map
- Dependency choices
- Release snapshot
- Integration acceptance

## Selection workflow

Start with the existing site's modules and configuration. Use the map to identify candidates, then verify selected releases, installed source and feature behavior. Treat the map as a starting point rather than an instruction to install all modules.

For each substantial feature, record the requirement, existing LMS configuration, candidate extension, actual dependency chain, uncovered behavior and acceptance evidence. Use `assets/feature-plan.md`. Prefer configuration or a small integration to replacing an available subsystem.

Distinguish documented capability from a proven fit. Check scoring, access, attempts, media, content portability and operational requirements when relevant. A dependency-resolution success alone does not prove these behaviors.

## Feature-to-module map

All project links below were reviewed on 2026-11-08. Verify current metadata and selected-release dependencies when using them.

| Product requirement | Candidate | Dependency/fit checks |
|---|---|---|
| Approve enrolment requests for selected courses | [LMS Membership Request](https://www.drupal.org/project/lms_membership_request) | Requires Group Membership Request; reconcile request/join permissions and class-based enrolment |
| Let learners submit files | [LMS File Upload](https://www.drupal.org/project/lms_file_upload) | Uses private files; configure storage, upload policy, access and evaluation needs |
| Put a structured form in an activity | [LMS Webform](https://www.drupal.org/project/lms_webform) | Requires Webform integration; verify submissions, scoring/completion and result visibility |
| Issue a course certificate | [LMS Certificate](https://www.drupal.org/project/lms_certificate) | Certificate framework; its FillPDF submodule needs configured FillPDF rendering |
| Design certificates as Drupal entities/templates | [LMS Certificate Entity](https://www.drupal.org/project/lms_certificate_entity) | Requires LMS Certificate; Entity Print supplies the documented PDF path |
| Send event-related student/teacher messages | [LMS Messages](https://www.drupal.org/project/lms_messages) | Requires Message; verify delivery configuration and membership-request interaction |
| Move complete courses as YAML/ZIP packages | [LMS YAML](https://www.drupal.org/project/lms_yaml) | Verify importer/exporter version, actual package schema and media/references |
| Use authored xAPI packages and LMS tracking | [LMS Xapi](https://www.drupal.org/project/lms_xapi) | Evaluate supported package/runtime behavior and the minimal LRS against reporting needs |
| Add H5P activities | [LMS H5P](https://www.drupal.org/project/lms_h5p) | Depends on LMS Xapi and H5P; verify LRS configuration and content-specific scoring |
| Deliver SCORM packages | [LMS Scorm](https://www.drupal.org/project/lms_scorm) | Provides upload/player/answer integration; test the required SCORM edition and real package |
| Migrate an Opigno installation | [LMS Migrate](https://www.drupal.org/project/lms_migrate) | Provides migration examples/plugins; inspect source versions, mappings, relationships and files |

Find machine-readable metadata, source URLs and review dates in `source-index.json`. Treat listed supporting packages as dependencies to inspect, not a substitute for Composer metadata and enabled-module checks.

## Dependency choices

### Certificates

Use LMS Certificate as the common integration layer. Evaluate one rendering path against the product's requirements:

- Use the FillPDF submodule when filling an existing PDF form template is appropriate; configure the FillPDF module and rendering backend/service.
- Use LMS Certificate Entity when Drupal entities, fields and templates suit the certificate design; add/configure Entity Print and its PDF renderer for PDF output.

Do not describe Certificate Entity as independent of LMS Certificate, assume both rendering paths are necessary, or build a custom PDF subsystem before evaluating these options. Verify completion/pass eligibility, authorized retrieval, attempt/reissue behavior and retained fields with the selected path.

### H5P and xAPI

Account for LMS, H5P, LMS H5P, LMS Xapi and LRS configuration. The H5P project page describes xAPI-based responses and automatic LMS scoring when configured. Test the actual content type, resume/state behavior and score/completion mapping; avoid promising identical results for every H5P library.

The main LMS ecosystem page describes xAPI package integration and a minimal LRS. Validate the required authored package and LRS capabilities against installed source; do not assume this is a complete external learning-record platform.

### Approvals and messages

LMS Membership Request requires Group Membership Request. Verify that immediate self-join cannot bypass approval. Test messages around request, approval, rejection and enrolment only for events actually supported by the selected versions.

The LMS Messages page retains a warning linked to [issue 3507217](https://www.drupal.org/project/grequest/issues/3507217). The issue is fixed in [Group Membership Request 3.2.4](https://www.drupal.org/project/grequest/releases/3.2.4). Check the selected dependency before reusing a patch; do not automatically apply an old patch or treat the stale warning as an unresolved blocker.

### Portability and migration

Use LMS YAML for supported LMS course packages. Use LMS Migrate for the migration paths it actually supplies, especially Opigno examples. Do not imply either is a universal Moodle, SCORM, xAPI or arbitrary-YAML importer.

Preserve source identifiers/mappings, relationships, referenced files, membership and attempts according to migration scope. Test imports with representative content in a development site and inspect duplicate/update behavior before repeated imports.

## Release snapshot

Use these observations for initial evaluation only. Recheck the selected release before adding a dependency.

| Project | Release shown on 2026-11-08 | Compatibility shown | Advisory/maintenance observation |
|---|---|---|---|
| LMS Membership Request | 1.1.0-beta4 | Drupal ^10.3 or ^11 | No supported stable release; minimally maintained |
| LMS File Upload | 1.0.2 | Drupal ^10 or ^11 | Stable release displays coverage |
| LMS Webform | 1.0.0-beta2 | Drupal ^10.3 or ^11 | Project says no advisory coverage; LMS 1.1.3+ noted |
| LMS Certificate | 1.0.0-alpha3 | Drupal ^10.3 or ^11 | No supported stable release reported |
| LMS Certificate Entity | [1.0.x-dev](https://www.drupal.org/project/lms_certificate_entity/releases/1.0.x-dev) | Drupal ^10 or ^11 | Development release; project says no advisory coverage |
| LMS Messages | [1.1.0-alpha3](https://www.drupal.org/project/lms_messages/releases/1.1.0-alpha3) | Drupal ^10 or ^11 | Project says no advisory coverage |
| LMS YAML | 2.0.0-beta3 | Drupal ^11 | Project says no advisory coverage |
| LMS Xapi | 1.0.0-beta1 | Drupal ^10.3 or ^11 | Project says no advisory coverage; work in progress |
| LMS H5P | 1.0.0-alpha4 | Drupal ^10.3 or ^11 | Project says no advisory coverage |
| LMS Scorm | 1.1.1 | Drupal ^10 or ^11 | Stable release; project says no advisory coverage |
| LMS Migrate | 1.0.0-alpha2 | Drupal ^10 or ^11 | Project says no advisory coverage |

Retrieved project pages can be cached; a release-page check already corrected a stale Messages observation during this review. Avoid selecting an older release merely to match this table. Check the release's LMS dependency line as well as Drupal compatibility. Present material tradeoffs without automatically replacing a suitable module with custom code.

## Integration acceptance

Verify the whole dependency chain for a selected feature. Include configuration, permissions and relevant learner/teacher behavior in a real course attempt. Check combinations that affect each other, such as membership requests and messages or package completion and certificates.

Report the selected module/release, configuration performed, remaining custom work and evidence. Mark research-only candidates and runtime-unverified integrations clearly.
