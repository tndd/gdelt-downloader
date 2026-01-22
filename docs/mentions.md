# GDELT 2.0 Mentions Database (mentions.CSV)

Mentions データベースは、Eventsデータベースに記録されたイベントが「どの記事で、いつ、どのように言及されたか」を記録します。
1つのイベントに対して複数の「言及（Mention）」が存在する可能性があります。

## カラム定義

| Index | Column Name | Type | Description |
| :--- | :--- | :--- | :--- |
| 0 | GLOBALEVENTID | INTEGER | EventsテーブルのIDへの外部キー |
| 1 | EventTimeDate | INTEGER | イベントが最初に追加された日時 |
| 2 | MentionTimeDate | INTEGER | この言及が検知された日時 (15分刻み) |
| 3 | MentionType | INTEGER | ソースタイプ (1=WEB, 2=CITATIONONLY, 3=CORE, 4=DTIC, 5=JSTOR, 6=NONTEXTUALSOURCE) |
| 4 | MentionSourceName | STRING | ソース名 (例: "nytimes.com") |
| 5 | MentionIdentifier | STRING | 記事の一意な識別子 (通常はURL) |
| 6 | SentenceID | INTEGER | イベントが言及された文の番号 |
| 7 | Actor1CharOffset | INTEGER | Actor 1 の文字オフセット |
| 8 | Actor2CharOffset | INTEGER | Actor 2 の文字オフセット |
| 9 | ActionCharOffset | INTEGER | Action の文字オフセット |
| 10 | InRawText | INTEGER | 生テキスト内で発見されたか (1=Yes) |
| 11 | Confidence | INTEGER | 抽出の信頼度 (0-100) |
| 12 | MentionDocLen | INTEGER | ソース記事の長さ（文字数） |
| 13 | MentionDocTone | FLOAT | 記事全体のトーン |
| 14 | MentionDocTranslationInfo | STRING | 翻訳情報（該当する場合） |
| 15 | Extras | STRING | 追加情報を含むXML |
