# Repository guidance

This repository contains the source of one portable `drupal-lms` skill. It is not a Drupal application.

- Preserve one short `SKILL.md` router and three focused workflow references.
- Evaluate existing configuration and ecosystem modules before custom code.
- Keep canonical sources, review dates and runtime/source limits explicit.
- Do not change dated release observations without checking their primary source.
- Keep all bundled paths portable and link reference files directly from `SKILL.md`.
- Keep assistant-local installation artifacts, credentials and unrelated project files outside this repository.
- Run `python3 tools/validate_repository.py` and `python3 -m unittest discover -s tests -v` after relevant changes.
- Report documentation, source and runtime verification separately. Do not claim installation or publication from local files alone.
