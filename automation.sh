#!/bin/bash

# =================================================================
# GDELT 日次ダウンロード・ラッパースクリプト
# =================================================================

# プロジェクトのルートディレクトリ（絶対パスに変更することを推奨）
PROJECT_DIR="/Users/tau/Repository/my_gdelt"
LOG_DIR="$PROJECT_DIR/logs"
DATE=$(date +%Y%m%d)

# ログディレクトリの作成
mkdir -p "$LOG_DIR"

# 1. プロジェクトディレクトリへ移動
cd "$PROJECT_DIR" || exit

# 2. 仮想環境の有効化
source venv/bin/activate

# 3. ダウンローダーの実行
# 引数なしで実行するとデフォルトで「今日」のデータが対象になります
echo "[$(date)] Starting GDELT download for $DATE..." >> "$LOG_DIR/download_$DATE.log"
python3 gdelt_downloader.py >> "$LOG_DIR/download_$DATE.log" 2>&1

echo "[$(date)] Finished." >> "$LOG_DIR/download_$DATE.log"
