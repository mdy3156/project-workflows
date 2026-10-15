# A small checkpoint

Use this only when the project has no suitable task owner. It is a suggested
shape, not a schema. Omit fields that do not affect recovery. Write into the
target project, never into the installed skill directory.

```markdown
# Short task name

Updated: date/time with timezone. State: active, blocked, paused, or complete.

## Goal and boundaries

Outcome and completion conditions. Constraints that still affect execution.
Link a design, issue, or specification instead of copying it.

## Current state

Repository/worktree and branch; relevant revision and dirty work.
Completed work with evidence. Unfinished work, failures, or a concrete blocker.
For live jobs: actual service/job/run ID, last observed status and time,
launch config/source references, outputs and how to check the job again.

## Next action

One actionable next step, its prerequisite, and how to recognize success.
Keep any remaining checklist here; do not maintain a second task inventory.

## Knowledge and evidence

Links to surviving experiment/research/architecture records, test evidence,
and external artifacts. Explicitly identify unavailable or local-only evidence.
```

Prefer a stable task name across sessions, not a new file for each date or agent.
Keep task-specific designs beside the task or in the planner's existing location.
Do not create a new permanent `decisions.md`, `progress.md`, or `findings.md` when
this one file suffices. If those files are already part of the chosen planner,
respect their roles and link to each owner rather than duplicating state.

For example, “collect outputs from the existing evaluation run after querying
its scheduler; validate all expected shards before marking complete” is a useful
next action. “Continue experiments” is not. If the job's configuration cannot
be recovered, write that constraint explicitly rather than filling in today's
local config.

For a checkpoint to survive loss of the workspace itself, it needs the project's
authorized durable storage, usually committed and pushed Git history or an
existing task service. A file saved only on one machine survives session loss,
not loss of that machine. Review it for secrets before sharing; do not upload
session transcripts, environment dumps, or credential-bearing job commands.
