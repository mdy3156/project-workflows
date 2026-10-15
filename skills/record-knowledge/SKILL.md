---
name: record-knowledge
description: Use when recording an experiment, investigation, or implemented architecture as durable project knowledge, including failed or interrupted runs and reproducibility evidence. Not for temporary plans or routine progress updates.
license: MIT
---

# Record knowledge

Leave the smallest accurate record that another person can understand and use
without this conversation. Write in the project's language and existing layout.
The installed skill contains guidance; all records belong in the target project.

## Choose the owner

Read the project's instructions, documentation entry point, and relevant code or
evidence. Search for an existing record of this topic or run before creating one.
Extend that record when it answers the same question. Avoid a report per tool
call, session, seed, or rerun; a coherent comparison can hold several run IDs.

| Knowledge | Content | Default when no convention exists |
| --- | --- | --- |
| Architecture | What the code currently implements | `docs/architecture/<topic>.md` |
| Experiment | What was actually tried, observed, and concluded | `docs/experiments/<date>-<topic>.md` |
| Research | A sourced investigation or synthesis across evidence | `docs/research/<topic>.md` |

Create only the needed file. Use an existing README as the entry point; add a
small `docs/README.md` only when navigation needs it. Indexes contain links and
brief purpose, not copied metrics, conclusions, or task status.

## Record evidence, then interpretation

- **Architecture:** inspect the relevant implementation and tests. Explain
  boundaries, data flow, and important constraints with source paths or symbols
  and the inspected revision. Qualify dirty or unverified code. Future designs
  belong in the task's plan, not in the description of the current system.
- **Experiment:** capture the question, actual conditions, outcomes, and limits.
  Connect the run to its configuration, source, data, evaluation, and artifacts.
  Read [record shapes](references/records.md) when composing a record, especially
  for dirty source trees, multiple commits, or unavailable artifacts.
- **Research:** state the question, scope, findings and evidence, contradictions,
  and what can be concluded. Distinguish observed facts from inference. Cite
  original sources and relevant experiment records; add access dates or versions
  for changing sources. Preserve negative results and alternative explanations.

Use the existing tracker, database, manifests, and configs as their respective
sources of truth. Keep selected evidence and interpretation in Markdown, with
enough identity and retrieval context to find the original. Do not export whole
run registries or duplicate logs into a second tracking system.

Record actual resolved settings and overrides; today's config and Git HEAD may
not describe yesterday's run. Separate generation/training and analysis commits
when they differ. Missing provenance is an explicit gap, not a field to guess.
Only claim completion, causality, or improvement supported by the measurements
and comparable evaluation conditions. Keep interrupted, failed, and unevaluated
work distinguishable from successful results.

## Finish

Check important numbers, IDs, units, denominators, source links, and availability
claims against evidence. When you cannot verify something, say what is missing.
Keep credentials and sensitive data out of records and URLs; record a safe
locator or an explicit access limitation instead.

Link related knowledge without copying its contents. Put remaining execution
steps in the existing task tracker or plan and link it only if useful. A small
correction belongs in the current record; a wider consolidation is a separate
curation pass. Report the record changed and any material evidence gaps.
