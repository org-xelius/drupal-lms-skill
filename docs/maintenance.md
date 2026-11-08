# Maintaining the skill

Keep the skill portable and focused. Maintain one short router and three workflow references, with detailed source material loaded only when relevant.

## Change the right file

| Change | Update |
|---|---|
| Scope, routing or shared behavior | `skills/drupal-lms/SKILL.md` |
| Course/development/plugin procedure | The corresponding file in `skills/drupal-lms/references/` |
| Ecosystem capability or dependency choice | `references/ecosystem.md` and relevant `references/source-index.json` observations |
| Review date or canonical source | `references/source-index.json` and affected reference text |
| Reusable output format | The corresponding template in `skills/drupal-lms/assets/` |
| Skill display name or invocation example | `skills/drupal-lms/agents/openai.yaml` |
| Inspector behavior | `scripts/inspect_project.py` and meaningful checks under `tests/` |
| Reader-facing setup or usage | Root README and `docs/` |
| npx distribution or directory metadata | `docs/distribution.md`, `skills.sh.json` and `tools/check_skills_install.py` |

Paths shortened to `references/` or `scripts/` in this table are relative to `skills/drupal-lms/`.

## Refresh source evidence

Refresh affected sources when adopting the skill into a product, upgrading dependencies or finding a documentation discrepancy. Inspect current primary project/release pages and the actual installed source. Update review dates and observations together.

Keep the registry's selected-release and verification fields truthful. A metadata refresh does not establish a tested installation. Do not mark exact APIs or runtime behavior verified without corresponding evidence.

The registry currently indexes three official guides and 29 linked chapters, plus 11 ecosystem projects. If upstream adds/removes chapters or the agreed scope changes, update both the registry and relevant completeness checks in the validator.

Preserve attribution and canonical URLs. Keep copied upstream material within its applicable licensing terms; this repository does not include the LMS source tree.

## Validate a change

From the repository root:

```bash
python3 tools/validate_repository.py
python3 -m unittest discover -s tests -v
python3 tools/check_skills_install.py
git diff --check
```

The validator checks metadata, portability, documentation links, source completeness, Python syntax, directory configuration and CI structure. Inspector tests check read-only behavior. The Skills CLI check verifies discovery and an isolated project installation, including supporting files. GitHub Actions runs these checks on pushes and pull requests; configuration does not establish a completed remote run.

The install check pins Skills CLI 1.7.6. Review its current Node requirements, commands and behavior before changing that pin, then update distribution guidance and rerun the check. Test telemetry stays disabled. Use real public-repository installations, rather than smoke-test counts, for skills.sh discovery; see [distribution](distribution.md).

For workflow changes, exercise a representative request using the revised skill. Check that it loads the appropriate references, evaluates existing modules, preserves project boundaries and reports verification limits. Use fresh task context for an independent check when it would expose a meaningful failure mode.

Update the [validation record](../VALIDATION.md) with checks actually completed and material remaining limits. Avoid replaying expensive tests when a small documentation change only needs relevant link and structural checks, unless repository instructions require them.

## Keep publication reviewable

Review changed files and stage the intended source/documentation only. Keep credentials, local installations, dependency folders, generated caches and unrelated project files out of the repository.

Confirm the destination branch and existing remote history before publishing. Preserve existing remote work; do not force-push or replace unknown history to simplify the initial import. Follow repository protections if they require a pull request.

Installing a new skill version into an assistant remains separate from pushing the source. Verify installation through the supported workflow after the version is selected.
