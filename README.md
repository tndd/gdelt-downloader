# GDELT 2.0 データダウンローダー

GDELT 2.0 Project からニュースデータを効率的に取得し、分析しやすい Parquet 形式で保存するための Python ツールです。

## 特徴

- **高速なパース**: `polars` を採用し、巨大な CSV データも高速に読み込みます。
- **効率的なストレージ**: 解凍後のデータを `Parquet` 形式（カラム指向型）で保存するため、ディスク容量を節約し、後の分析（SQLなど）が爆速になります。
- **並列ダウンロード**: 15分刻みのファイルを複数スレッドで同時に取得します。
- **スキーマ自動適用**: 各カラムに意味のある名前（`GLOBALEVENTID`, `SOURCEURL` など）を自動で付与します。

## セットアップ

### 環境準備

Python 3.8以上が必要です。

```bash
# クローンまたはディレクトリ移動後
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 依存ライブラリ
- `requests`: 通信用
- `polars`: データ処理
- `tqdm`: 進捗表示
- `duckdb`: ローカル分析用

## 使い方

メインスクリプト `gdelt_downloader.py` を実行します。

```bash
# 今日の最新データをすべて取得
python3 gdelt_downloader.py

# 特定の日付のデータを取得 (YYYYMMDD)
python3 gdelt_downloader.py --date 20260121

# 特定のデータ種別のみ取得 (events, mentions, gkg)
python3 gdelt_downloader.py --type events

# 【NEW】期間を指定して一括取得
# 2024年1月1日から1月31日までを取得（--workers で並列数指定可）
python3 gdelt_downloader.py --start-date 20240101 --end-date 20240131 --workers 16

# 【WARNING】全期間のデータを取得（テラバイト級のサイズになります）
# ※このモードでは自動的に並列数が 16 に設定されます
python3 gdelt_downloader.py --full-history

# 動作テスト（最初の3件のみ取得）
python3 gdelt_downloader.py --limit 3
```

### データの保存場所
実行すると、カレントディレクトリに `data/` フォルダが作成され、以下のように分類されます。
- `data/events/`: イベントデータ
- `data/mentions/`: 報道の言及データ
- `data/gkg/`: ナレッジグラフ（詳細文脈）データ

## データの活用方法 (DuckDB / Polars)

保存された Parquet ファイルは、そのまま SQL や Python で超高速に分析できます。
詳細は **[データ分析・活用ガイド](docs/analysis.md)** をご覧ください。

### クイック分析例:
```bash
# Python (Polars) で国別集計を実行
python3 analyze_sample.py

# DuckDB (SQL) で全件の合計を算出
duckdb -c "SELECT COUNT(*) FROM 'data/events/*.parquet';"
```

## 各データセットの概要

詳細は `docs/` ディレクトリ内の各ドキュメントを参照してください。

1. **[Events](docs/events.md)** (export): 「いつ・誰が・どこで・何をしたか」というイベントの記録。
2. **[Mentions](docs/mentions.md)**: そのイベントがどのメディアで報じられたかの詳細レポート。
3. **[Global Knowledge Graph](docs/gkg.md)** (GKG): 人名、組織名、テーマ（テロ、経済など）、数千種類の感情指標を網羅した詳細データ。

---
このプロジェクトは GDELT Project の公開データを利用しています。
詳細な仕様は [GDELT Project](https://www.gdeltproject.org/) を参照してください。
