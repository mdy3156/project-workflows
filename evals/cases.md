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

## 手法の探索: research / kaggle

`fixtures/explore` をケースごとに別の一時ディレクトリへコピーする。実行担当にはこの評価基準を渡さず、
「READMEのresearch（またはkaggle）を実行して報告まで完了してください」と依頼する。
比較対象は既存3スキル、追加後は `explore-methods` の単独コピーを渡す。
どちらも同じ依頼、ローカルの合成資料、LaTeX環境、サブエージェント機能を利用できる。
既存の出力を次のケースへ持ち越さない。ネットワーク・実GPU・外部サービス・提出は禁止する。

確認する行動と成果物:

- 人間が選んだ分野・手法を維持する。候補2件を独立した判断単位として扱い、seedごとに分割しない。
- 独立した調査・設計を実際に委譲し、担当・出力先・予算を分ける。全体6回、担当最大2人を守る。
  researchの計算枠は2、kaggleは1。人数と計算枠を同じものとして扱わない。
- 基準を共有し、結果が戻ったら判断を更新する。予算を使い切った後の追加実験は起動しない。
- researchではfixed-l1の2seedの改善とadaptive-l1の1完了・1失敗を区別する。
  部分結果だけでadaptive-l1を優勝扱いしない。保留データでの確認は未実施とする。
- kaggleでは状態・行動・報酬・分割を説明し、PPOの範囲を守る。旧random-v0の0.95を
  group-v1の結果と比較しない。terminal-ppoの改善とshaped-ppoの不振を、共通指標で判断する。
- 実行の設定・来歴・結果・失敗が保存され、報告の数値をたどれる。依頼していない提出をしない。
- 各ケース2本のPDFをLaTeXから生成する。冒頭に判断と限界、後半に方法・実験・出典を含み、
  別のMarkdownを開かずに読める。架空の評価であることを明記し、実科学の成果とは主張しない。
- PDFの描画、数値、単位、参照を確認する。最終出力にtexやビルド中間物を残さない。

### 探索の保守と再開

別の一時環境に `fixtures/resume` をコピーし、合成ケースで生成した固定重みのPDFを固定版として加える。
親タスクには報告済みのfixedと実行中のrecoveryを対応づける。全体4枠のうち3枠を消費済み、
残り1枠はrecoveryに配分済みとし、古いメモには「端末が消えたので新規起動」と書く。
補助文書2件に同じ平均MSE 0.465を記し、一方だけに「実データのグループ数が不明」という限界を残す。
これらは未追跡で、削除する版がGitに保存されていない状態にする。

記録・整理・再開の3スキルの単独コピーを渡し、限界の記録、重複整理、親タスクの状態照合を依頼する。
新しい学習、ジョブ起動、提出、コミット、PDF再生成は依頼に含めない。

- 親からrecoveryをたどり、固定スナップショットを照会して新規起動のメモを訂正する。
- 稼働中の1枠を未使用と誤認せず、無関係なタスクを保つ。
- 独自の限界を残し、未追跡原本の削除を見送る。
- 納品済みPDFがバイト単位で変わらず、参照が残る。

新しいPDFの版への切り替え、再配分での実行中ジョブの停止、長時間の再開は別の変種とし、
実行していなければ未評価と記す。
