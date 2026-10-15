# Record shapes

These are prompts for deciding what matters, not a mandatory schema. Use the
relevant shape, omit inapplicable fields, and keep missing critical evidence
explicit. Reuse project names and identifiers rather than creating a new ID system.

## Experiment

A readable record usually answers:

1. What question or hypothesis was tested? What changed and what was held fixed?
2. Which runs and exact conditions produced these observations?
3. What happened, including failures, exclusions, and incomplete work?
4. What does the comparison support, and what does it leave unresolved?

For reproducibility, retain the following information or precise references to
records that own it:

| Evidence | What makes the reference useful |
| --- | --- |
| Run identity | Tracker/project namespace plus run ID or an actual run URL; without a tracker, the project's existing result path or manifest |
| Source | Generating commit and source state; for dirty source, a retained patch/snapshot including relevant untracked code, or an explicit unrecoverable gap |
| Configuration | Versioned config plus resolved overrides or immutable resolved config; the invocation when needed to reconstruct execution |
| Data and environment | Data/model versions or fingerprints, preprocessing recipe, split membership/protocol, seeds, runtime/lockfile and material hardware constraints |
| Evaluation | Metric definition, units, direction, population/denominator, selection versus held-out evaluation, comparator and uncertainty when available |
| Outcomes | Planned versus completed work, measured results, stop/failure reason, and relevant cost or resource use |
| Artifacts | Actual storage locator, version/checksum when available, and whether the artifact is retained, local-only, inaccessible, or lost |

An exact reference to a retained run manifest can cover most of this table.
Inspect it before relying on it; an unreachable service is not verified evidence.
Do not invent a URI scheme, checksum, run ID, or successful upload. A local path
can be recorded as a code-formatted locator with its machine/storage context and
availability; it is not a portable download link. Avoid private host details in
public documentation. Git preserves tracked text, not ignored datasets, external
runs, or missing weights. Missing artifacts can limit reproduction even with a
complete description.

For separate generation and analysis, identify both revisions and the input
artifact consumed by the analysis. Do not replace the generating revision with
the documentation commit. A config hash alone does not recover its contents.
Retain the resolved config or a retrievable immutable reference. For commands
containing secrets, retain safe options and credential-variable names, not values.

If recording an already authorized running experiment, save its run/job identity
and known launch provenance before waiting. Use the task checkpoint for live job
status. Finalize the durable record when evidence arrives. A proposed run with no
execution evidence remains a plan. Recording a run does not authorize rerunning it.

### Compact example (synthetic)

> The `cache-window` comparison used runs `bench/control-6` and `bench/window-6`
> from the same retained manifest. The candidate changed the cache window only;
> both used requests-v2, split-A, seed 11, and 2,000 requests at concurrency 8.
> P95 latency was 61 ms versus 58 ms. One repetition does not establish a stable
> improvement. A concurrency-64 attempt failed after 300 requests with a lock
> error; it has no final latency. Its settings and failure remain part of this
> comparison. The manifest pins the code and resolved configs; raw traces were
> local-only and are now lost, so the reported quantiles cannot be re-audited.

Do not copy example identifiers or results into a real record.

## Architecture

Use a stable topic filename. Explain the current responsibility, inputs/outputs,
important collaborators and constraints. Link to the relevant source and tests;
note the inspected revision and any unverified area. Include design rationale
only where it still explains the current implementation. Update this explanation
after the code changes; do not append obsolete versions or migration diaries.

## Research

Use a stable question or topic filename. State the scope, source versions/dates,
findings, conflicting evidence, and conclusion with its limitations. Link each
material claim to a source or experiment. When results differ by protocol,
population, or code revision, retain that distinction instead of averaging or
choosing the newest result. Correct a disproven claim explicitly with evidence;
do not silently turn a historical observation into a different result.
