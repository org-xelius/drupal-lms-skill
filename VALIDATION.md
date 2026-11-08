# Validation record

Date: 2026-11-08.

This record describes checks completed against the local source; it is not a statement of current remote publication or directory-listing status.

## Completed checks

| Check | Observed result |
|---|---|
| Skill frontmatter and UI metadata | Parsed with a real safe YAML parser; required fields and default invocation pass |
| Router size and portable references | 68-line router; all 16 local links resolve within the skill |
| Repository documentation | Getting-started, usage, product-planning, maintenance and distribution guides; all local documentation links validated |
| Source registry | Three guide trees, 29 linked chapters and all 11 requested ecosystem projects |
| Python syntax | All five Python source/test files parse successfully |
| Automated regression checks | 18 tests pass: project inspection, malformed metadata, discovery, copied bundles, directory metadata and portable file links |
| CI configuration | YAML, push/PR triggers, read-only repository permissions, Node setup and check commands pass local validation |
| Skills CLI compatibility | CLI 1.7.6 discovers drupal-lms and installs it into a temporary Codex project; all 15 bundled files match their source bytes |
| Directory-page metadata | skills.sh.json has valid expected fields and refers to the actual skill name |
| Install visibility | The first README shell block is the canonical npx install command; the prepared GitHub About text includes the same command |

The inspector distinguishes declared, locked and installed dependency evidence; preserves unknown enabled/runtime state; supports custom webroot/vendor paths; rejects malformed metadata; preserves input files; and avoids unrelated settings. Additional checks reject false discovery matches, missing/extra/changed installed files, copy-mode symlinks, broken/escaping file links and malformed directory metadata.

## Cleanup review

Consolidated duplicated link checks and JSON loading. The inspector now rejects an installed-package object with no package list rather than reporting an empty installed inventory. The installer requires an actual discovery row and an exact copied bundle. YAML/directory metadata failures use clear validation errors.

The README was reduced from 84 to 37 lines, with the npx command immediately after the introduction. Contributor setup lives in maintenance; installation flags/authentication live in distribution. The GitHub About payload is prepared locally, with a documented application step; it has not been applied to live repository metadata.

## npx distribution verification

The installation check used an existing official Skills CLI 1.7.6 entry point with Node.js 26.13.0. It listed the local source, installed a copy into a temporary Codex project and compared all 15 bundled files. Test telemetry was disabled and the temporary project was removed.

The default npx launcher was also attempted, but this workspace could not resolve registry.npmjs.org. The locally available CLI therefore verified discovery/installation behavior; fresh npm package retrieval was not verified. CI is configured to run the same check through npx using the pinned CLI and Node.js 24.

No public GitHub install, public repository-visibility check, telemetry ingestion, skills.sh listing or page-cache refresh was verified. The new directory metadata and README badge do not establish those outcomes.

## Workflow trials

Fresh task contexts used the skill and its bundled references without being given expected answers. No files or live Drupal systems were changed by these trials.

| Request | Observed behavior |
|---|---|
| Three-unit community reporting course with quizzes, uploaded evidence, teacher reflection, cohorts and certificates | Produced an authoring blueprint; selected existing answer plugins, Classes, File Upload and certificate candidates; left upload grading and runtime compatibility unverified |
| Approval, notifications, H5P, locally rendered PDF certificates and course portability | Selected Membership Request/Group Membership Request, Messages/Message, H5P/Xapi, Certificate/Certificate Entity/Entity Print and LMS YAML; kept custom PHP conditional |
| Ordering five steps with partial credit and feedback before final submission | Evaluated existing H5P content first; defined a native plugin fallback and configuration/test contract; did not claim exact PHP signatures without source |

These trials demonstrate useful routing and reuse decisions for the supplied scenarios. They do not establish reliability for every future request.

## Source corrections from review

- Refreshed the stale Messages project snapshot using its 1.1.0-alpha3 release page.
- Recorded Certificate Entity's 1.0.x-dev candidate and declared Drupal 10/11 compatibility from the release page.
- Confirmed that Group Membership Request 3.2.4 includes the fix for issue 3507217; retained an instruction to inspect the selected dependency rather than apply an old patch.

See the source registry for canonical URLs and dates.

## Remaining limits

- No Drupal application, resolved dependency graph, enabled-module inventory or learner/teacher runtime was available.
- The LMS code host was unavailable, so exact installed API signatures remain to be checked in a product environment.
- The creator's bundled quick validator was attempted but could not import PyYAML in this workspace. The repository validator independently parsed the actual YAML with system Ruby/Psych and checked the bundle, links and source registry.
- GitHub Actions has been configured but has not run on a remote repository.
- Account-wide skill installation and remote publication are not established by these local source checks.
