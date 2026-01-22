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

# 3. ダウンローダーの実行 (Docker経由)
echo "[$(date)] Starting GDELT download for $DATE..." >> "$LOG_DIR/download_$DATE.log"

# make download を実行
# ※ PATH等の問題で make が見つからない場合はフルパス指定か docker-compose を直接呼ぶように修正してください
/usr/bin/make download >> "$LOG_DIR/download_$DATE.log" 2>&1

echo "[$(date)] Finished." >> "$LOG_DIR/download_$DATE.log"
