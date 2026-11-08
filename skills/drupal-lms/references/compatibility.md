# Compatibility and evidence

## Establish the baseline

Inspect `composer.json`, `composer.lock`, installed-package metadata, enabled modules and affected source. Resolved lockfile versions do not prove that dependencies are installed, nor that Drupal modules are enabled.

```bash
python3 /path/to/drupal-lms/scripts/inspect_project.py /path/to/drupal-project
```

Check the actual Drupal root and execution convention before Composer or Drush commands. Use the existing environment; do not assume DDEV, Docker or a `web/` directory.

## Interpret documentation by date

The project page reviewed on 2026-11-08 lists LMS 1.2.5, released 2026-11-02, compatible with Drupal `^10.3 || ^11`. Its release page recommends the `^1.2` Composer line. Treat this as a research snapshot, not a permanent installation constraint.

The 1.2.5 notes introduce lesson-specific activity parameters through `ActivityParametersInterface` and extend training initialization. Inspect source when these affect the task; older examples may omit them.

Sources: [project](https://www.drupal.org/project/lms), [1.2.5 release](https://www.drupal.org/project/lms/releases/1.2.5).

Resolve PHP, database and Group requirements from selected releases. An older LMS guide's PHP minimum does not establish the requirements of newer Drupal core.

## Check extensions

Record selected releases and Composer dependency constraints, including the LMS line. Confirm module names and optional submodules from `.info.yml` files. Check documented interactions and relevant issues.

Distinguish stability, security-advisory coverage and maintenance. Stable does not itself imply advisory coverage; project-level coverage does not imply pre-release coverage. Explain the actual deployment tradeoff without a universal prohibition on pre-release modules.

Preview dependency resolution only after choosing a real constraint, using the project's workflow. Avoid broad updates, global stability changes and guessed pins.

## Resolve conflicts

1. Inspect the installed interface, base class, service definition or configuration.
2. Compare release notes and canonical documentation.
3. Record the discrepancy and implement against the actual version.
4. Check the relevant behavior in the project environment.

If source/runtime access is absent, label the result as a documented design or candidate implementation. Code-host access during initial research was unavailable; the bundle does not certify exact 1.2.5 source signatures.
