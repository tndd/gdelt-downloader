# 自動実行ガイド

このスクリプトを毎日決まった時間に自動実行（差分更新）する方法を説明します。
macOS では主に `cron` または `launchd` を使用します。

## 事前準備: ラッパースクリプト

自動実行用には、仮想環境の有効化とログ記録をセットで行う `automation.sh` を使用するのが最も簡単です。

1.  `automation.sh` 内の `PROJECT_DIR` が正しい絶対パスになっていることを確認してください。
2.  実行権限を与えます（設定済みですが念のため）:
    ```bash
    chmod +x automation.sh
    ```

## 方法1: cron を使う (推奨: 最もシンプル)

`cron` は Unix 系の標準的な定期実行ツールです。

1.  ターミナルで `crontab -e` を実行します。
2.  エディタが開くので、以下の行を追加します（毎日 午前2時に実行する場合）:

```cron
0 2 * * * /Users/tau/Repository/my_gdelt/automation.sh
```

-   `0 2 * * *`: 毎日午前 2時 0分に実行。
-   パスは必ず**絶対パス**で記述してください。

---

## 方法2: launchd を使う (macOS の標準方式)

macOS で推奨されている高度な管理方法です。PCがスリープしていた場合、次に復帰した際に実行するといった制御が可能です。

1.  `~/Library/LaunchAgents/com.user.gdelt_downloader.plist` というファイルを以下の内容で作成します。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.user.gdelt_downloader</string>
    <key>ProgramArguments</key>
    <array>
        <string>/Users/tau/Repository/my_gdelt/automation.sh</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>2</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>/Users/tau/Repository/my_gdelt/logs/launchd_out.log</string>
    <key>StandardErrorPath</key>
    <string>/Users/tau/Repository/my_gdelt/logs/launchd_err.log</string>
</dict>
</plist>
```

2.  以下のコマンドでエージェントを有効化します:
    ```bash
    launchctl load ~/Library/LaunchAgents/com.user.gdelt_downloader.plist
    ```

---

## 正常に動作しているか確認する

自動実行設定後、`logs/` ディレクトリに日付ごとのログファイルが生成されていれば正常です。

```bash
cat logs/download_20260122.log
```

---

## 補足：なぜ毎日自動で動くのか？（仕組みの解説）

これらのプログラムは**常駐プログラム（デーモン）**と呼ばれる仕組みを利用しています。

### Cron の場合
Unix系OSには `cron` (crond) というプログラムがバックグラウンドで24時間常に動いています。
- 彼は1分に1回目を覚まし、「設定ファイル（crontab）」を確認します。
- 「今の時刻」と「設定された時刻」が一致すれば、指定されたコマンドを実行します。

### Launchd の場合
macOS専用の管理システムです。OSの一部として深く組み込まれており、`cron` より賢い制御が可能です。
- PCがスリープしていて実行時間を過ぎてしまった場合でも、スリープ復帰時に「あ、実行し忘れてた！」と気づいて実行してくれます（設定によります）。
