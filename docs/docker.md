# Docker による自動実行ガイド

Docker を使用すると、OSごとの違い（cronやパス設定など）を気にせず、コマンド一つで環境構築と自動実行スケジュールの設定が完了します。

## 前提条件

- Docker Desktop (または Docker Engine) がインストールされていること

## 使い方

### 1. 起動（バックグラウンド実行）

以下のコマンドで、毎日午前2時に自動実行するスケジューラーが起動します。

```bash
docker-compose up -d --build
```
    
### 【重要】手動で特定の量のデータをダウンロードする場合

（例：全量は多すぎるので、直近のデータ 10GB程度分だけ欲しい場合）
1ファイル圧縮時2MB計算で5000ファイル取得すると、解凍・Parquet変換後でおおよそ数GB〜10GB程度になります。

```bash
# --limit 5000 を指定して実行
docker-compose run gdelt-downloader python gdelt_downloader.py --full-history --limit 5000
```

これだけで完了です。
- 必要なライブラリが自動でインストールされたコンテナが起動します。
- 毎日 **午前 02:00** にダウンローダーが自動実行されます。
- データはホスト側の `data/` ディレクトリに保存（マウント）され続けます。

### 2. コンテナの状態確認

```bash
docker-compose ps
```

### 3. ログの確認

実行ログ（いつダウンロードしたか）を確認するには：

```bash
docker-compose logs -f
```

### 4. 停止

```bash
docker-compose down
```

## 設定の変更

実行時間を変更したい場合は `scheduler.py` の以下の行を編集し、再度 `docker-compose up -d --build` してください。

```python
schedule.every().day.at("02:00").do(job)
```
