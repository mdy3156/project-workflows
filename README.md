# Project Workflows

人間が決めた研究分野・改善方針の中で、エージェントが候補の調査、設計、実験、知見の報告まで
進めるためのAgent Skillsです。独立した作業を並列に進め、結果に応じて次の実験を選びます。
人間が最初に読む成果物は、**手法ごとに1本の判断用PDF**です。

## 人間とエージェントの役割

| 用途 | 人間が決めること | エージェントが進めること |
| --- | --- | --- |
| 新しい研究 | Diffusion Model、Lassoなどの分野・対象、目的と制約 | 分野内の候補調査、仮説、設計、小実験、筋のよい方針の評価 |
| Kaggle | PPOを使うなどの大きな改善方針、目的と制約 | 適用方法の設計、候補の比較実験、追加検証、知見の報告 |

探索の途中で、人間の選んだ分野や大きな方針を勝手に変えません。範囲と予算が決まっていれば、
その中の候補選択や実験の採否はエージェントが判断します。

Diffusion Modelの候補Aと候補Bは、採否を別々に判断するならPDFを2本作ります。
同じ候補のseedやハイパーパラメータ違いはその候補のPDFにまとめ、共通のベースラインも比較条件として示します。

## 入口と補助スキル

| Skill | 役割 | 主な成果物 |
| --- | --- | --- |
| [explore-methods](skills/explore-methods/SKILL.md) | 候補を分け、調査・設計・実験を配分し、結果から次を判断する | 手法ごとのPDF、根拠の記録、探索の状態 |
| [record-knowledge](skills/record-knowledge/SKILL.md) | 実験・調査・実装済みの構造を根拠とともに記録する | 再利用できるMarkdownと実行への参照 |
| [curate-knowledge](skills/curate-knowledge/SKILL.md) | 重複した知識を統合し、根拠を保って整理する | 整理した文書と参照 |
| [continue-work](skills/continue-work/SKILL.md) | 親子タスク・実行・成果物を照合して作業を再開する | 既存の計画に保存した現在地と次の行動 |

新しい探索は `explore-methods` から始めます。ほかの3つは記録、整理、再開だけを頼むときにも使えます。
各Skillは単独で導入でき、相互の呼び出しは必須ではありません。

## 使い方

```text
$explore-methods Diffusion Modelで、少数の学習データでも性能を保つ方法を探索してください。
独立して採否を判断できる候補を調査・実験し、手法ごとに日本語の判断用PDFを作ってください。
計算予算は合計8 GPU時間、同時実験は2件までです。既存の評価分割を使ってください。
```

```text
$explore-methods このKaggleコンペでPPOを使う方針です。
適用方法を設計し、予算内で候補を比較して、手法ごとの判断用PDFにまとめてください。
計算枠はGPU1台、合計4時間です。コンペへの提出は含めません。
```

```text
$continue-work 保存した探索を再開してください。親タスクから各候補と稼働中ジョブを確認してください。
$record-knowledge 今回の実験の条件、結果、失敗、再現できない部分を記録してください。
$curate-knowledge この話題の補助文書を整理し、判断用PDFと実験の根拠を保ってください。
```

数値は呼び出し例です。実際の予算・評価方法・期限は利用するプロジェクトで決めます。
必要な条件が欠けていれば、エージェントが調査を進めながら確認します。

## 並列探索と報告

親の担当が依存関係、全体予算、担当ごとの出力先を管理し、利用環境のサブエージェントやジョブ機能へ
作業を配分します。戻った結果から追加検証や打ち切りを決め、異なる評価分割のスコアを混ぜて順位を付けません。
担当人数と計算枠は別々に管理します。GPUが1台なら、調査・設計を並列化しながら実験は順に実行できます。
並列機能のない環境でも同じ判断手順で順に進められますが、並列実行したとは報告しません。

PDFの最初のページには、手法の要点、有望かどうかの判断、主要な比較結果、負担、限界を載せます。
関心があれば、同じPDFの後半で仕組み、実験条件、失敗を含む結果、出典、再現情報を読めます。
読者は指定分野の基礎を知っていますが、候補の詳細や過去の会話を知らなくても理解できる構成です。

報告はLaTeXで生成し、文字と全ページの描画を確認してPDFを納品します。生成用texやビルド中間物は
一時領域で扱い、編集原稿として残す必要はありません。納品済みPDFは固定し、再報告が必要な場合は
新しい版を作ります。入口には各手法の現在の1本を案内します。

PDF生成には対象言語に対応したLaTeX環境とフォント、描画確認用ツールが必要です。
日本語ならLuaLaTeX等、描画確認にはPoppler等を使えます。生成できない場合はPDF納品を未完了として伝えます。
Skills自体はMarkdownであり、常駐runnerや新しい実験管理サービスを導入するものではありません。

## 情報の置き場所

既存の配置を優先します。配置がない場合は、必要なファイルだけ次の形で作れます。

```text
reports/<topic>/    手法ごとの固定版PDF
docs/research/     出典と調査の補助記録
docs/experiments/  条件、結果、失敗、再現情報
docs/architecture/ 現在のコードの説明
.work/<topic>.md   探索全体の状態、候補と担当、予算、次の行動
```

モデル、データ、ログ、設定は既存の保存先に残します。MarkdownとPDFは根拠に接続し、現在の設定を
過去の実行条件の代わりにしません。保存されていない変更や消失した成果物は欠落として明記します。
既存の計画管理があれば再利用し、同じ進捗を別の台帳へ複製しません。

## インストール

Codexの `$skill-installer` に、使いたいSkillの導入を依頼できます。

```text
$skill-installer で mdy3156/project-workflows の
skills/explore-methods、skills/record-knowledge、skills/curate-knowledge、skills/continue-work をインストールしてください。
```

リモート導入は、変更が公開された後に使えます。このcheckoutの内容をWSL2/Linuxで共通利用する場合は、
リポジトリ直下で以下を実行します。同名の導入があると `ln -sT` は上書きせず失敗します。

```bash
mkdir -p "$HOME/.agents/skills"
for workflow_skill in explore-methods record-knowledge curate-knowledge continue-work; do
  ln -sT "$PWD/skills/$workflow_skill" "$HOME/.agents/skills/$workflow_skill"
done
```

他の環境では使うSkillのフォルダ全体をSkills保存先へコピーします。このリポジトリ自身では
`.agents/skills/` のリンクから同じ実体を参照します。導入先の設定を自動変更する処理はありません。
リンクはcheckoutの変更を直接反映するため、安定した版を使う場合は確認済みcommitからコピーしてください。

## 開発と検証

配布検査にはPython 3.11以上を使います。

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python -m unittest discover -s tests -v
```

公式 `skills-ref` の固定commitで形式を検証し、各Skillの単独コピー、ライセンス、メタデータ、
インラインのローカルリンクを検査します。外部URLの到達性や見出しanchorは検査の対象外です。
行動は別に[合成ケース](evals/cases.md)で確認し、範囲と限界を[評価記録](evals/results.md)に残します。
合成ケースは実際の研究成果やコンペ性能を証明するものではありません。

設計は[構成と設計判断](docs/architecture.md)、以前の調査は[調査と出典](docs/research.md)にあります。

## ライセンス

[MIT License](LICENSE)。各Skillにも単独配布用のLICENSEを同梱しています。
Privateプロジェクトの文書・コード・データは含みません。
