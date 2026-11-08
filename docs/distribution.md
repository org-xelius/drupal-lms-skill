# Distribution with npx and skills.sh

Use Vercel's existing Skills CLI to install this GitHub-hosted skill. The repository already uses a standard discovery location: `skills/drupal-lms/SKILL.md`, with the required `name` and `description` frontmatter. A separate npm package for this repository is not required.

## Install from GitHub

Run in the product project:

```bash
npx skills add org-xelius/drupal-lms-skill --skill drupal-lms
```

For Codex, select the agent explicitly:

```bash
npx skills add org-xelius/drupal-lms-skill --skill drupal-lms --agent codex
```

Add `--global` for user-level scope. To inspect available skills without installing, use:

```bash
npx skills add org-xelius/drupal-lms-skill --list
```

The tested CLI is `skills@1.7.6`, which declares Node.js `>=22.20.0`; CI uses Node.js 24. Pin the CLI version when reproducing the test environment. Pin a published repository tag or commit when a team needs a fixed skill revision; the CLI version and skill revision are separate choices.

Primary references: [installation and options](https://github.com/vercel-labs/skills/blob/main/docs/commands.md), [skill discovery](https://github.com/vercel-labs/skills/blob/main/docs/creating-skills.md).

## Understand skills.sh listing

The [skills.sh FAQ](https://skills.sh/docs/faq) says directory entries are populated through installation telemetry from the CLI. A GitHub push or adding a configuration file alone does not establish a listing. A legitimate installation from the published repository, with normal telemetry enabled, supplies that signal. Allow time for processing and caching; verify the actual listing rather than claiming instant publication.

The CLI [telemetry guidance](https://github.com/vercel-labs/skills/blob/main/docs/troubleshooting.md#telemetry) says GitHub repository/skill identifiers are sent only when the repository is confirmed public. Public directory discovery therefore requires a publicly readable source. Private repositories remain installable for authorized users, but are not a route to public indexing through that telemetry. This setup does not change repository visibility.

Do not generate artificial installations to increase rankings. Local smoke tests use telemetry disabled and are evidence of compatibility only.

## Directory-page metadata

The root [skills.sh.json](../skills.sh.json) groups `drupal-lms` under Drupal LMS product development. It is optional display metadata; the standard `skills/` layout supplies CLI discovery.

The [customization guide](https://skills.sh/docs/customize) says public repository-page settings are refreshed after a CLI install with telemetry enabled. Changes can be cached. The README badge links to the expected repository page and does not certify that a listing already exists.

## Authentication for private repositories

The CLI supports existing Git credentials and SSH. If HTTPS access fails but your authorized SSH connection works, use the source explicitly:

```bash
npx skills add git@github.com:org-xelius/drupal-lms-skill.git --skill drupal-lms --agent codex
```

This still requires repository access; npx does not grant missing GitHub permissions or bypass an access denial. Refer to the upstream installation guide for authentication behavior.

## Verify a local checkout

List the local skill without fetching this repository:

```bash
npx skills add . --list
```

Run the isolated installation check:

```bash
python3 tools/check_skills_install.py
```

It uses the pinned CLI, a temporary source copy and a temporary Codex project. It checks discovery, installation and byte-for-byte preservation of the supporting files, then removes the temporary project. It does not install into your account's skill directories or send test installation telemetry.

The check can use an already available official CLI for offline verification:

```bash
python3 tools/check_skills_install.py --cli /absolute/path/to/skills/bin/cli.mjs
```

The supplied CLI must report the pinned version. This verifies the same CLI behavior while skipping the npx package-download step; report that distinction in validation results.

## Update an installed copy

Use `npx skills check` to inspect updates and `npx skills update drupal-lms` to update the selected skill. Verify the installation after updates. These commands manage installed copies separately from editing or pushing this source repository.
