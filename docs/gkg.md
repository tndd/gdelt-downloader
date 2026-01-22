# GDELT 2.0 Global Knowledge Graph (gkg.CSV)

GKG データベースは、ニュース記事の「文脈」を詳細に記録したナレッジグラフです。
人名、組織名、場所、テーマ、感情など、イベント構造に収まらない非構造的な情報を含みます。

## カラム定義

| Index | Column Name | Type | Description |
| :--- | :--- | :--- | :--- |
| 0 | GKGRECORDID | STRING | GKGレコードの一意なID (YYYYMMDDHHMMSS-<SOURCE>-<ID>) |
| 1 | DATE | INTEGER | ファイルの日付 (YYYYMMDDHHMMSS) |
| 2 | SourceCollectionIdentifier | INTEGER | ソースコレクションID |
| 3 | SourceCommonName | STRING | ソースの一般名 |
| 4 | DocumentIdentifier | STRING | ドキュメント識別子 (URL) |
| 5 | Counts | STRING | カウント情報リスト ("CountType#Num#ObjectType#...") |
| 6 | V2Counts | STRING | 拡張カウント情報 |
| 7 | Themes | STRING | テーマ一覧 (セミコロン区切り) |
| 8 | V2Themes | STRING | 拡張テーマ一覧 (オフセット付き) |
| 9 | Locations | STRING | 場所一覧 (セミコロン区切り) |
| 10 | V2Locations | STRING | 拡張場所一覧 (オフセット付き) |
| 11 | Persons | STRING | 人名一覧 (セミコロン区切り) |
| 12 | V2Persons | STRING | 拡張人名一覧 (オフセット付き) |
| 13 | Organizations | STRING | 組織名一覧 (セミコロン区切り) |
| 14 | V2Organizations | STRING | 拡張組織名一覧 (オフセット付き) |
| 15 | Tone | STRING | トーン情報ブロック (Tone, Pos, Neg, Polarity, AR, SOG) |
| 16 | EnhancedDates | STRING | テキスト内の日付参照 |
| 17 | GCAM | STRING | Global Content Analysis Measures (数千種類の感情分析スコア) |
| 18 | SharingImage | STRING | シェアイメージのURL |
| 19 | RelatedImages | STRING | 関連画像のリスト |
| 20 | SocialImageEmbeds | STRING | ソーシャルメディア画像埋め込み |
| 21 | SocialVideoEmbeds | STRING | ソーシャルメディア動画埋め込み |
| 22 | Quotations | STRING | 抽出された引用文 |
| 23 | AllNames | STRING | 全固有名詞リスト |
| 24 | Amounts | STRING | 金額等の数量情報 |
| 25 | TranslationInfo | STRING | 翻訳メタデータ |
| 26 | ExtrasXML | STRING | 追加抽出データを含むXML blob |
