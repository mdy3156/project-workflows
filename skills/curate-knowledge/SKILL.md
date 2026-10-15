---
name: curate-knowledge
description: Use when project documentation has overlapping findings, stale architecture, scattered experiment knowledge, or completed plans to retire, and the user wants consolidation or cleanup. Not for merely recording one new result.
license: MIT
---

# Curate knowledge

Reduce the reading needed to understand a topic while retaining its evidence.
Work in the requested scope, using the project's language and conventions.
The target is useful knowledge, not an arbitrary document count.

## Find what belongs together

Read the documentation entry point and relevant project instructions. Inspect
Git status, including untracked files, before editing. Search by question,
component, dataset, evaluation protocol, run ID, and source symbol, not just
filenames or dates. Read connected records and their evidence before selecting
the surviving owner of each topic. Do this inventory in working context; do not
create a permanent inventory or a second knowledge registry.

Keep the roles clear:

| Kind | Surviving owner should explain |
| --- | --- |
| Architecture | Current implementation, verified against source and tests |
| Experiment | Actual conditions, observations, failures, and reproducibility |
| Research | Synthesis across evidence, including disagreement and limits |
| Task/design | Unfinished work and future intent, kept in its existing planner |

Prefer updating an established topic document. Related experiments can share a
comparison record; do not flatten independent run conditions into one result.
An entry point should remain navigation, not become a copy of all four kinds.
No new directory structure is required for a project that already has one.

## Integrate without changing the evidence

For each candidate, decide whether to keep, correct, merge, or retire it. Move
unique facts into their surviving owner before removing the old text. Preserve
failed attempts, negative findings, caveats, and unresolved contradictions.
Different splits, populations, revisions, or metrics can explain conflicting
results; recency alone does not decide which is true.

Verify current architecture from the code. Historical experiments retain their
original execution conditions. A new analysis may correct an interpretation,
but must identify its evidence and leave the original observation intelligible.
Research should link to experiment evidence rather than duplicate all run tables.

For every merged experiment, retain the run namespace/ID, generating and analysis
revisions, actual config/overrides, data and evaluation identity, outcome, and
retrievable artifact or manifest references needed to reconstruct it. If an
external tracker is unavailable, retain the surviving local evidence and mark
the gap. A high-level conclusion cannot replace the only reproduction recipe.

## Retire safely

Remove a document only when all of these are true:

- It is within the cleanup scope and no longer owns unique useful information.
- Its important evidence is available from the surviving documents and their
  verified references; neither Git history alone nor an unchecked remote service
  substitutes for discoverable current evidence.
- The version being removed is recoverable in Git. For untracked files or
  uncommitted edits, preserve that version in an authorized commit first, or
  keep the original and report the remaining cleanup. Do not commit unrelated
  work or assume permission to commit/push.
- Incoming links and plain-text path references in docs, plans, instructions,
  and code have been repaired. Check anchors when headings move too.

Delete retired Markdown rather than creating an archive, tombstone, or duplicate
summary. Keep unfinished plans. Retire a completed plan only after its useful
implementation knowledge, results, and open questions have surviving owners.
Knowledge cleanup does not authorize deleting configs, raw data, artifacts,
tracker entries, source code, or unrelated user notes.

For example, merge two descriptions of one successful run, but retain the
failed high-concurrency attempt and its sole invocation in the surviving
experiment. Update the architecture separately from those historical results.

Finish by reviewing the diff, remaining references, and whether a new reader
can locate both the conclusion and its evidence. Report the owners updated,
documents removed, and specific evidence or history gaps that prevented cleanup.
