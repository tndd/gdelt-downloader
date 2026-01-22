# GDELT 2.0 Events Database (export.CSV)

Events データベースは、「いつ・誰が・誰に・何をしたか」というイベントの核となる情報を記録しています。
1イベントにつき1行が生成されます。

## カラム定義

| Index | Column Name | Type | Description |
| :--- | :--- | :--- | :--- |
| 0 | GLOBALEVENTID | INTEGER | 全イベントで一意のID |
| 1 | SQLDATE | INTEGER | 日付 (YYYYMMDD) |
| 2 | MonthYear | INTEGER | 年月 (YYYYMM) |
| 3 | Year | INTEGER | 年 (YYYY) |
| 4 | FractionDate | FLOAT | 年の経過率としての浮動小数点型日付 |
| 5 | Actor1Code | STRING | Actor 1 のCAMEOコード |
| 6 | Actor1Name | STRING | Actor 1 の名称 |
| 7 | Actor1CountryCode | STRING | Actor 1 の3文字国コード |
| 8 | Actor1KnownGroupCode | STRING | Actor 1 の既知グループコード |
| 9 | Actor1EthnicCode | STRING | Actor 1 の民族コード |
| 10 | Actor1Religion1Code | STRING | Actor 1 の宗教コード1 |
| 11 | Actor1Religion2Code | STRING | Actor 1 の宗教コード2 |
| 12 | Actor1Type1Code | STRING | Actor 1 のタイプコード1 |
| 13 | Actor1Type2Code | STRING | Actor 1 のタイプコード2 |
| 14 | Actor1Type3Code | STRING | Actor 1 のタイプコード3 |
| 15 | Actor2Code | STRING | Actor 2 のCAMEOコード |
| 16 | Actor2Name | STRING | Actor 2 の名称 |
| 17 | Actor2CountryCode | STRING | Actor 2 の3文字国コード |
| 18 | Actor2KnownGroupCode | STRING | Actor 2 の既知グループコード |
| 19 | Actor2EthnicCode | STRING | Actor 2 の民族コード |
| 20 | Actor2Religion1Code | STRING | Actor 2 の宗教コード1 |
| 21 | Actor2Religion2Code | STRING | Actor 2 の宗教コード2 |
| 22 | Actor2Type1Code | STRING | Actor 2 のタイプコード1 |
| 23 | Actor2Type2Code | STRING | Actor 2 のタイプコード2 |
| 24 | Actor2Type3Code | STRING | Actor 2 のタイプコード3 |
| 25 | IsRootEvent | INTEGER | ルートイベントかどうか (1=Yes) |
| 26 | EventCode | STRING | CAMEOイベントコード |
| 27 | EventBaseCode | STRING | ベースCAMEOコード |
| 28 | EventRootCode | STRING | ルートCAMEOコード |
| 29 | QuadClass | INTEGER | 1=Verbal Coop, 2=Material Coop, 3=Verbal Conflict, 4=Material Conflict |
| 30 | GoldsteinScale | FLOAT | イベントの影響度 (-10 to +10) |
| 31 | NumMentions | INTEGER | このイベントへの言及総数 |
| 32 | NumSources | INTEGER | 言及したソースの総数 |
| 33 | NumArticles | INTEGER | 言及した記事の総数 |
| 34 | AvgTone | FLOAT | 言及記事の平均トーン |
| 35 | Actor1Geo_Type | INTEGER | Actor 1 の場所タイプ |
| 36 | Actor1Geo_FullName | STRING | Actor 1 の場所名称 |
| 37 | Actor1Geo_CountryCode | STRING | Actor 1 の場所国コード |
| 38 | Actor1Geo_ADM1Code | STRING | Actor 1 の場所ADM1コード |
| 39 | Actor1Geo_Lat | FLOAT | Actor 1 の場所緯度 |
| 40 | Actor1Geo_Long | FLOAT | Actor 1 の場所経度 |
| 41 | Actor1Geo_FeatureID | STRING | Actor 1 の場所GNS/GNIS ID |
| 42 | Actor2Geo_Type | INTEGER | Actor 2 の場所タイプ |
| 43 | Actor2Geo_FullName | STRING | Actor 2 の場所名称 |
| 44 | Actor2Geo_CountryCode | STRING | Actor 2 の場所国コード |
| 45 | Actor2Geo_ADM1Code | STRING | Actor 2 の場所ADM1コード |
| 46 | Actor2Geo_Lat | FLOAT | Actor 2 の場所緯度 |
| 47 | Actor2Geo_Long | FLOAT | Actor 2 の場所経度 |
| 48 | Actor2Geo_FeatureID | STRING | Actor 2 の場所GNS/GNIS ID |
| 49 | ActionGeo_Type | INTEGER | アクション発生場所のタイプ |
| 50 | ActionGeo_FullName | STRING | アクション発生場所の名称 |
| 51 | ActionGeo_CountryCode | STRING | アクション発生場所の国コード |
| 52 | ActionGeo_ADM1Code | STRING | アクション発生場所のADM1コード |
| 53 | ActionGeo_Lat | FLOAT | アクション発生場所の緯度 |
| 54 | ActionGeo_Long | FLOAT | アクション発生場所の経度 |
| 55 | ActionGeo_FeatureID | STRING | アクション発生場所のGNS/GNIS ID |
| 56 | DATEADDED | INTEGER | データベース追加日 (YYYYMMDD) |
| 57 | SOURCEURL | STRING | ソース記事のURL |
