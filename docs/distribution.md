# Installation and skills.sh

The [Skills CLI](https://github.com/vercel-labs/skills) discovers this repository's `skills/drupal-lms/SKILL.md` and carries its references, assets and helper script into the selected agent.

## Install

Run from your product project:

```bash
npx skills add org-xelius/drupal-lms-skill --skill drupal-lms
```

| Option | Purpose |
|---|---|
| Default scope | Install into the current project; select agents when prompted |
| `--agent codex` | Select Codex explicitly |
| `--global` | Install at user scope across projects |
| `--copy` | Copy supporting files instead of choosing symlinks |
| `--list` | Inspect the repository's available skills without installing |

The tested CLI is `skills@1.7.6`, requiring Node.js `>=22.20.0`; CI uses Node.js 24. Pin the CLI to reproduce its test environment, and pin a published repository tag or commit when a team needs a fixed skill revision. These are separate version choices.

See the upstream [command reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md) and [discovery rules](https://github.com/vercel-labs/skills/blob/main/docs/creating-skills.md).

## Private repositories

Use existing Git credentials or an authorized SSH connection:

```bash
npx skills add git@github.com:org-xelius/drupal-lms-skill.git --skill drupal-lms
```

Repository permissions still apply. The CLI does not grant access to a private source.

## Updates

```bash
npx skills check
npx skills update drupal-lms
```

These commands manage installed copies separately from editing or publishing this source repository.

## skills.sh discovery

The [directory FAQ](https://skills.sh/docs/faq) describes listing through CLI installation telemetry. The CLI sends GitHub identifiers only for [confirmed-public repositories](https://github.com/vercel-labs/skills/blob/main/docs/troubleshooting.md#telemetry). A legitimate public-source installation with telemetry enabled supplies the discovery signal; allow time for processing and caching, then verify the actual listing.

The root [skills.sh.json](../skills.sh.json) controls page grouping. It does not register the skill, change repository visibility or prove a listing exists. The README badge links to the expected page. See [page customization](https://skills.sh/docs/customize).

## Maintainer verification

The [maintenance guide](maintenance.md#validate) documents source checks, the pinned CLI installation check and its offline entry-point option. The check uses a temporary Codex project, disables test telemetry and compares the complete installed bundle. It does not install into your personal skill directories.
