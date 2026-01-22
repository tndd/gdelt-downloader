import polars as pl
import os

def analyze_gdelt_data():
    # 読み込み対象のディレクトリ
    events_dir = "data/events"
    
    if not os.path.exists(events_dir) or len(os.listdir(events_dir)) == 0:
        print(f"Error: {events_dir} にデータがありません。先にダウンローダーを実行してください。")
        return

    print("--- GDELT 分析サンプル (Polars) ---")
    print(f"フォルダ '{events_dir}' からデータを読み込み中...")

    # Lazy読込により、全データをメモリに乗せずに処理を構築
    # ※ *.parquet で全ファイルを対象にする
    query = (
        pl.scan_parquet(f"{events_dir}/*.parquet")
        .filter(pl.col("ActionGeo_CountryCode").is_not_null())
        .group_by("ActionGeo_CountryCode")
        .agg([
            pl.len().alias("event_count"),
            pl.col("GoldsteinScale").mean().alias("avg_impact"),
            pl.col("NumMentions").sum().alias("total_mentions")
        ])
        .sort("event_count", descending=True)
        .limit(10)
    )

    # 実際に計算を実行
    result = query.collect()

    print("\n[世界を賑わせている国 Top 10]")
    print(result)

    print("\n分析のヒント:")
    print("- GoldsteinScale: 数値が高いほどその国にとってポジティブな報道、低いほどネガティブな報道です。")
    print("- total_mentions: 報道の総量。イベント1つが多数のメディアで報じられると増えます。")

if __name__ == "__main__":
    analyze_gdelt_data()
