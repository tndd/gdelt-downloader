# Docker による自動実行ガイド

Docker を使用すると、OSごとの違い（cronやパス設定など）を気にせず、コマンド一つで環境構築と自動実行スケジュールの設定が完了します。

## 前提条件

- Docker Desktop (または Docker Engine) がインストールされていること

## 使い方

### 1. 起動（バックグラウンド実行）

プロジェクトのルートディレクトリで以下のコマンドを実行します。

```bash
docker-compose up -d --build
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
