# GDELT 2.0 データダウンローダー

GDELT 2.0 Project からニュースデータを効率的に取得し、分析しやすい Parquet 形式で保存するための Python ツールです。
Docker を使用して環境構築不要ですぐに実行可能です。

## 特徴

- **環境構築不要**: Docker で全て完結します。
- **高速なパース**: `polars` を採用し、巨大な CSV データも高速に読み込みます。
- **効率的なストレージ**: 解凍後のデータを `Parquet` 形式（カラム指向型）で保存するため、ディスク容量を節約し、後の分析（SQLなど）が爆速になります。
- **並列ダウンロード**: 15分刻みのファイルを複数スレッドで同時に取得します。

## セットアップ

Docker および Docker Compose がインストールされている必要があります。

```bash
# ビルド
make build
```

## 使い方 (Makefile)

便利な `make` コマンドを用意しています。

```bash
# 今日の最新データをダウンロード
make download

# 保存されたデータを分析 (サンプル分析)
make analyze

# シェルに入る (デバッグ用)
make shell
```

### スケジューラー (常駐モード)

毎日AM 2:00に定期実行するスケジューラーを起動します。

```bash
# バックグラウンドで起動
make up

# ログを表示
make logs

# 停止
make down
```

## 使い方 (Docker Compose 直接実行)

`make` が使えない環境では、以下のコマンドを使用してください。

```bash
# ダウンロード実行
docker-compose run --rm gdelt-downloader python src/gdelt_downloader.py

# 分析実行
docker-compose run --rm gdelt-downloader python src/analyze_sample.py

# 期間指定などのオプション付き実行
docker-compose run --rm gdelt-downloader python src/gdelt_downloader.py --date 20240101
```

### データの保存場所
実行すると、カレントディレクトリの `data/` フォルダにデータが保存されます。
- `data/events/`: イベントデータ
- `data/mentions/`: 報道の言及データ
- `data/gkg/`: ナレッジグラフデータ

## データの活用方法 (DuckDB / Polars)

保存された Parquet ファイルは、SQL や Python で超高速に分析できます。

### クイック分析例:
```bash
# サンプル分析を実行
make analyze
```

詳細は `docs/` ディレクトリ内の各ドキュメントを参照してください。

---
このプロジェクトは GDELT Project の公開データを利用しています。
詳細な仕様は [GDELT Project](https://www.gdeltproject.org/) を参照してください。
