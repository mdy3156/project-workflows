# Maintaining Project Workflows

This repository distributes independent Agent Skills under `skills/`.
Read `README.md` for usage and `docs/architecture.md` for the current design
when those files exist. Active work belongs in the selected `.work/` file.

- Keep skills short, self-contained, and usable without a specific tracker,
  model, plugin, or another skill being installed.
- Keep project facts in the user's project, never in the installed skill.
- Prefer decision guidance to new scripts or mandatory document schemas.
- Validate changed skills with the official reference validator and
  `python -m unittest discover -s tests -v`. Meaningful workflow changes also
  need the relevant isolated behavioral case in `evals/cases.md`.
- Fixtures are synthetic. Never replace them with private project exports,
  real run IDs, credentials, local host details, or user transcripts.
- Skills and maintainer documentation are MIT; preserve bundled license files.
