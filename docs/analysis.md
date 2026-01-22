# GDELTデータ分析ガイド

このプロジェクトで保存された Parquet ファイルは、以下のツールを使って非常に高速かつ柔軟に分析できます。

## 1. DuckDB (SQLによる分析)

[DuckDB](https://duckdb.org/) は Parquet ファイルの直接クエリに最適化されたデータベースです。インストールなし（CLIのみ）でも動作し、SQLite のような手軽さでテラバイト級のデータを扱えます。

### 起動と基本クエリ

```bash
# data/events 配下の全Parquetファイルを統合してクエリ
duckdb -c "SELECT * FROM 'data/events/*.parquet' LIMIT 10;"
```

### 応用：国別のイベント数集計

最もイベント数（報道数）が多い上位10カ国を調べます。

```bash
duckdb -c "
SELECT 
    ActionGeo_CountryCode, 
    COUNT(*) as event_count 
FROM 'data/events/*.parquet' 
WHERE ActionGeo_CountryCode IS NOT NULL 
GROUP BY ActionGeo_CountryCode 
ORDER BY event_count DESC 
LIMIT 10;
"
```

---

## 2. Python (Polars による高速処理)

Python で大規模データを扱う場合は、このプロジェクトでも使用している `Polars` が推奨されます。

### サンプルコード

`analyze_sample.py` という名前で保存して実行してください。

```python
import polars as pl
import glob

# データの読み込み（複数ファイルのワイルドカード指定が可能）
# lazy=True にすることで、メモリ消費を抑えつつ高速にスキャンできます
df = pl.scan_parquet("data/events/*.parquet")

# クエリの構築
# 例：金平均が高い（重要度が高い）イベントを抽出
result = (
    df.filter(pl.col("GoldsteinScale") > 5.0)
    .group_by("ActionGeo_CountryCode")
    .agg(pl.count().alias("high_impact_events"))
    .sort("high_impact_events", descending=True)
    .limit(10)
    .collect() # 最後に collect() するまで実際の処理は走りません
)

print("高インパクトな報道が多い上位10カ国:")
print(result)
```

---

## 3. その他の活用方法

- **Pandas**: `pd.read_parquet("data/events/")` で読み込めますが、メモリ消費が大きいため、まずは Polars でフィルタリングしてから `to_pandas()` するのが効率的です。
- **BIツール**: Tableau や Power BI などで Parquet フォルダをそのままソースとして読み込めます。
- **Jupyter Notebook**: 可視化（matplotlib/seaborn/plotly）と組み合わせて調査するのに最適です。
