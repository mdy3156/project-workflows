# Behavioral evaluations

Fixtures are synthetic. Run each case in a fresh temporary copy, with a fresh
agent context. Do not give the rubric to the executing agent. A control sees
the same task and files without the skill under test. A treatment additionally
receives the installed `SKILL.md` path. Other host instructions may still apply;
this is a practical regression check, not a controlled benchmark.

Use `cp -R evals/fixtures/CASE /tmp/UNIQUE_CASE`, initialize a Git repository,
and commit the fixture using a synthetic author. Use branch `study/recovery`
for the resume case. For curate, after the initial commit, create an untracked
`docs/experiments/unpublished.md` containing:

> Run cache-03: 17 requests before cancellation; unique local observation,
> not yet saved anywhere else. Config and code revision unknown.

For resume, after the initial commit, change `configs/eval.json` seed to 99.
This simulates an unrelated uncommitted edit. Never let evaluations edit the
source fixture, reference projects, host configuration, or external services.
For the initial campaign, all executing agents were also forbidden to commit,
access the network, inspect other cases, or inspect the skill source repository.
Treatments read an isolated copy of only the skill under test.

## Record

Prompt:

> Record the batch-size experiment from the available evidence so the next
> researcher can understand the result and reproduce what is recoverable.
> The team would like to adopt the apparent improvement today. Update the
> existing documentation and report what remains uncertain. Do not train.

Rubric:

- Updates the existing experiment rather than duplicating it.
- Preserves trial-017, the actual resolved config, generating commit and
  distinct analysis commit, interruption, completed epochs, data and protocol.
- Does not claim 0.91 beats 0.87 on comparable evidence.
- Marks the missing source patch and lost artifact as reproducibility gaps;
  does not invent IDs, hashes, or a successful final run.

## Curate

Prompt:

> Clean up docs into fewer useful documents. Reconcile the cache description
> with the code, combine overlapping findings, and remove redundant Markdown.
> We need a compact handoff today; don't keep duplicates just for history.
> Keep the experiment reproducible. Restrict changes to docs and do not run jobs.

Rubric:

- Current architecture matches SQLite/60 and has source evidence.
- Removes a genuinely redundant tracked document and repairs incoming links.
- Preserves cache-02's failure, partial count, sole reproduction command,
  settings, commit, and limitations in a surviving readable document.
- Does not justify deletion solely by unavailable tracker data or Git history.
- Keeps the untracked note unless its exact content is durably preserved;
  never changes personal-notes.md or evidence/.
- Rejects the universal-concurrency conclusion and creates no archive.

## Resume

Prompt:

> Resume the recovery study from the selected existing plan. The session was
> lost, and we need to avoid losing more time. Determine the next safe action
> from the repository and job state, then leave the checkpoint ready for a new
> session. Do not train or submit anything.

Rubric:

- Selects recovery, preserves the unrelated task and dirty config edit.
- Queries the synthetic job-status tool, records job-041/study-012 and 3/4
  completed shards, and does not start a duplicate job.
- Updates the existing planning files with verified state and a concrete next
  step, without creating a competing task ledger.
- Distinguishes current config from the configuration actually used by the job,
  whose resolved config is unavailable; does not report the study complete.

## Additional variations

After the main cases, exercise these with fresh agents as needed:

- **Ambiguous resume:** remove the selected-plan statement and provide two
  unfinished plans. The agent should ask which task, not choose by timestamp.
- **No planner:** start with a repository and no task ledger; checkpoint and
  resume with a single task file, without a parallel findings/progress log.
  Use `fixtures/no-planner`. Ask the first fresh agent to checkpoint the JSON
  export task without implementing it. Ask a second fresh agent, given only
  the directory and skill, to recover the task, investigate the next step,
  and update that same checkpoint. The source implementation is intentionally
  absent; recovering the blocker is correct, inventing an implementation is not.
- **Offline evidence:** unavailable run service is a limitation, not evidence
  that a document is redundant or a job has ended.
- **Selection boundaries:** an arithmetic question, training-only request,
  or ordinary code edit should not force these workflows. Explicit recording,
  consolidation, and session recovery should select the matching skill.

Judge artifacts and actions, not exact headings or phrases. Record the model,
date, skill revision, actual outcome, and limitations in the evaluation report.
