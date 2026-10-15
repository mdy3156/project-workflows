# Project Workflows

長期の開発・研究で、知識を整理し、実験の根拠を残し、セッションをまたいで作業を再開するためのAgent Skillsです。

ソフトウェア開発、機械学習研究、Kaggleを想定しています。特定のモデルや実験管理サービスには依存しません。
Skills自体はMarkdownと表示用メタデータだけで動きます。

## 3つの役割

| Skill | 使うとき | 残すもの |
| --- | --- | --- |
| [record-knowledge](skills/record-knowledge/SKILL.md) | 実験・調査を記録する、実装後の構造を説明する | 根拠をたどれるArchitecture・Experiment・Research |
| [curate-knowledge](skills/curate-knowledge/SKILL.md) | 重複した説明や散在する知見を統合する | 整理した正本と参照。役割を終えたMarkdownは削除 |
| [continue-work](skills/continue-work/SKILL.md) | 長い作業を始める、中断から再開する、引き継ぐ | 既存の計画へ保存した現在地と次の行動 |

Writerと統合担当は別々のSkillです。同じエージェントが順に担当でき、常設の複数エージェントは必要ありません。
Skillsは使う場面を教えるもので、導入しただけで定期実行されるものではありません。

## インストール

Codexの `$skill-installer` に次のように依頼できます。必要なSkillだけでも使えます。

```text
$skill-installer で mdy3156/project-workflows の
skills/record-knowledge、skills/curate-knowledge、skills/continue-work をインストールしてください。
```

WSL2/Linuxで、このcheckoutの変更を共通利用したい場合は、リポジトリ直下で以下を実行します。
同名のインストールがある場合、`ln -sT` は上書きせず失敗します。既存の導入方法を確認してから選んでください。

```bash
mkdir -p "$HOME/.agents/skills"
for workflow_skill in record-knowledge curate-knowledge continue-work; do
  ln -sT "$PWD/skills/$workflow_skill" "$HOME/.agents/skills/$workflow_skill"
done
```

他の環境では、使いたいSkillのフォルダ全体を各エージェントのSkills保存先へコピーしてください。
このリポジトリ自身では `.agents/skills/` のリンクから同じ実体を参照します。
ユーザー全体とプロジェクト内の両方へ同じSkillを入れる必要はありません。

Codexのローカル配置・シンボリックリンク・検出方法は
[OpenAIの公式ガイド](https://learn.chatgpt.com/docs/build-skills)に従っています。
追加したSkillが一覧に出ない場合はCodexを再起動してください。
共有リンクはcheckoutの変更を直接反映します。安定した版を固定したい場合は、確認済みcommitからコピーします。

## 使い方

```text
$continue-work この改善作業を、別セッションでも再開できる形で進めてください。

$record-knowledge 今回の実験結果を記録してください。
設定・実行commit・Run ID・成果物の所在と、未完了や失敗も残してください。

$curate-knowledge キャッシュに関するdocsを統合してください。
コードと説明を照合し、実験の再現情報を保って重複文書を整理してください。

$continue-work 評価実験の作業を再開してください。
保存済みの計画、Git差分、既存ジョブを確認して次の作業へ進んでください。
```

自動選択も可能ですが、長い作業の開始・引き継ぎや文書の整理では明示呼び出しが確実です。
導入先の既存ルールを尊重しながら自動利用したい場合は、そのプロジェクトの `AGENTS.md` に
「長い作業と再開はcontinue-work、結果の記録はrecord-knowledge、重複の整理はcurate-knowledgeを使う」
という運用を加えられます。本リポジトリは導入先の設定を自動変更しません。

## 知識と作業の置き場所

既存の配置があれば引き継ぎます。何もないプロジェクトでは次を出発点にし、必要なファイルだけ作ります。

```text
docs/
  architecture/   現在のコードの説明
  experiments/    実際の条件・結果・失敗・再現情報
  research/       調査や複数実験から得た知見
.work/
  <task>.md       未完了の作業、必要な設計、現在地、次の行動
```

MLflow、SQLite、結果manifestなどは引き続き実験情報の正本です。Markdownには解釈と必要な証拠を残し、
実際の設定、生成時と解析時のcommit、Run ID、データ・評価の版、成果物へ接続します。
存在しないIDや保存先は作らず、失われた成果物や未回収の変更は欠落として明記します。

Planning with Files、Superpowers、Issueなどを使用中なら、そこに現在地を補います。
同じ進捗を新しい台帳へ複製しません。完了したDesignや作業メモは必要な知識へ反映し、
参照とGit履歴を確認してから退役させます。独自archiveは作りません。

詳しくは[構成と設計判断](docs/architecture.md)、[調査と出典](docs/research.md)を参照してください。

## 開発と検証

Skillsを使うだけならPythonの準備は不要です。リポジトリを変更するときは、Python 3.11以上で実行します。

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python -m unittest discover -s tests -v
```

形式検証にはcommitを固定した公式 `skills-ref` を使います。各Skillを一時ディレクトリに単独コピーし、
メタデータ、同梱ライセンス、ローカル参照を検査します。CIでも同じ検査を実行します。
リンク検査は通常のインラインリンクのファイル存在を対象とし、外部URLの到達性や見出しanchorは検査しません。

行動は別に、合成プロジェクトで[記録・統合・再開のシナリオ](evals/cases.md)を実行します。
結果と検証範囲は[評価記録](evals/results.md)に残します。文言の一致だけでは、知識の正しさを検証できません。

チェックポイントが保護するのは最後に保存した状態です。保存前のクラッシュや成果物の消失まで復元するものではありません。
別端末や環境消失からの再開には、承認されたGit pushや既存の共有保存先が必要です。

## ライセンス

[MIT License](LICENSE)。各Skillにも単独配布用のLICENSEを同梱しています。
参考にしたPrivateプロジェクトの文書・コード・データは含みません。
