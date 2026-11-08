# Validation record

Date: 2026-11-08.

## Completed checks

| Check | Observed result |
|---|---|
| Skill frontmatter and UI metadata | Parsed with a real safe YAML parser; required fields and default invocation pass |
| Router size and portable references | 68-line router; all 16 local links resolve within the skill |
| Source registry | Three guide trees, 29 linked chapters and all 11 requested ecosystem projects |
| Python syntax | Inspector, repository validator and inspector tests parse successfully |
| Inspector behavior | Eight automated tests pass |
| CI configuration | YAML, push/PR triggers, read-only repository permissions and check commands pass local validation |

The inspector checks distinguish declared constraints, locked dependencies and installed-package metadata; preserve unknown enabled/runtime state; support a custom webroot/vendor path; reject malformed metadata; preserve input files; avoid unrelated settings; and report a missing root as an error.

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
