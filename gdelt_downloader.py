import os
import requests
import polars as pl
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
import datetime
import zipfile
import io
import argparse

MASTER_LIST_URL = "http://data.gdeltproject.org/gdeltv2/masterfilelist.txt"
DATA_DIR = "data"

# Schema Definitions
SCHEMAS = {
    "events": [
        "GLOBALEVENTID", "SQLDATE", "MonthYear", "Year", "FractionDate", "Actor1Code", "Actor1Name",
        "Actor1CountryCode", "Actor1KnownGroupCode", "Actor1EthnicCode", "Actor1Religion1Code", "Actor1Religion2Code",
        "Actor1Type1Code", "Actor1Type2Code", "Actor1Type3Code", "Actor2Code", "Actor2Name", "Actor2CountryCode",
        "Actor2KnownGroupCode", "Actor2EthnicCode", "Actor2Religion1Code", "Actor2Religion2Code", "Actor2Type1Code",
        "Actor2Type2Code", "Actor2Type3Code", "IsRootEvent", "EventCode", "EventBaseCode", "EventRootCode",
        "QuadClass", "GoldsteinScale", "NumMentions", "NumSources", "NumArticles", "AvgTone", "Actor1Geo_Type",
        "Actor1Geo_FullName", "Actor1Geo_CountryCode", "Actor1Geo_ADM1Code", "Actor1Geo_Lat", "Actor1Geo_Long",
        "Actor1Geo_FeatureID", "Actor2Geo_Type", "Actor2Geo_FullName", "Actor2Geo_CountryCode", "Actor2Geo_ADM1Code",
        "Actor2Geo_Lat", "Actor2Geo_Long", "Actor2Geo_FeatureID", "ActionGeo_Type", "ActionGeo_FullName",
        "ActionGeo_CountryCode", "ActionGeo_ADM1Code", "ActionGeo_Lat", "ActionGeo_Long", "ActionGeo_FeatureID",
        "DATEADDED", "SOURCEURL"
    ],
    "mentions": [
        "GLOBALEVENTID", "EventTimeDate", "MentionTimeDate", "MentionType", "MentionSourceName",
        "MentionIdentifier", "SentenceID", "Actor1CharOffset", "Actor2CharOffset", "ActionCharOffset",
        "InRawText", "Confidence", "MentionDocLen", "MentionDocTone", "MentionDocTranslationInfo", "Extras"
    ],
    "gkg": [
        "GKGRECORDID", "DATE", "SourceCollectionIdentifier", "SourceCommonName", "DocumentIdentifier",
        "Counts", "V2Counts", "Themes", "V2Themes", "Locations", "V2Locations", "Persons", "V2Persons",
        "Organizations", "V2Organizations", "Tone", "EnhancedDates", "GCAM", "SharingImage", "RelatedImages",
        "SocialImageEmbeds", "SocialVideoEmbeds", "Quotations", "AllNames", "Amounts", "TranslationInfo", "ExtrasXML"
    ]
}

def fetch_master_list():
    """Fetches the latest master file list from GDELT."""
    print("Fetching master file list...")
    response = requests.get(MASTER_LIST_URL)
    response.raise_for_status()
    
    lines = response.text.strip().split('\n')
    data = []
    for line in lines:
        parts = line.split()
        if len(parts) == 3:
            size, hash_val, url = parts
            data.append({"size": int(size), "hash": hash_val, "url": url})
    
    df = pl.DataFrame(data)
    df = df.with_columns([
        pl.col("url").str.split("/").list.get(-1).alias("filename")
    ])
    df = df.with_columns([
        pl.col("filename").str.extract(r"(\d{14})").alias("timestamp_str"),
        pl.col("filename").str.contains("export").alias("is_events"),
        pl.col("filename").str.contains("mentions").alias("is_mentions"),
        pl.col("filename").str.contains("gkg").alias("is_gkg")
    ])
    
    return df

def download_and_convert(row, target_dir):
    """Downloads a ZIP file, extracts CSV, and converts to Parquet."""
    url = row['url']
    filename = row['filename']
    timestamp = row['timestamp_str']
    
    data_type = "unknown"
    if row['is_events']: data_type = "events"
    elif row['is_mentions']: data_type = "mentions"
    elif row['is_gkg']: data_type = "gkg"
    
    if data_type == "unknown":
        return False

    parquet_filename = f"{timestamp}.{data_type}.parquet"
    target_path = os.path.join(target_dir, data_type, parquet_filename)
    
    if os.path.exists(target_path):
        return False

    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    
    try:
        r = requests.get(url)
        r.raise_for_status()
        
        with zipfile.ZipFile(io.BytesIO(r.content)) as z:
            csv_filename = z.namelist()[0]
            with z.open(csv_filename) as f:
                content = f.read()
                if not content:
                    return False
                
                # Use schema if available
                columns = SCHEMAS.get(data_type)
                
                # GDELT v2 files are tab-separated. 
                # We use truncate_ragged_lines because some GKG/Mentions lines can be weird.
                df = pl.read_csv(
                    content, 
                    has_header=False, 
                    separator="\t", 
                    new_columns=columns,
                    truncate_ragged_lines=True,
                    ignore_errors=True,
                    encoding="utf8-lossy"
                )
                
                df.write_parquet(target_path)
                return True
    except Exception as e:
        print(f"Error processing {url}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="GDELT 2.0 Downloader")
    parser.add_argument("--date", type=str, help="Date in YYYYMMDD format (default: today)", default=datetime.datetime.now().strftime("%Y%m%d"))
    parser.add_argument("--type", type=str, choices=["all", "events", "mentions", "gkg"], default="all", help="Data type to download")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of files to download (for testing)")
    
    args = parser.parse_args()
    
    # 1. Fetch master list
    master_df = fetch_master_list()
    
    # 2. Filter by date
    filtered_df = master_df.filter(pl.col("timestamp_str").str.starts_with(args.date))
    
    # 3. Filter by type
    if args.type != "all":
        # Argument 'events' matches column 'is_events', etc.
        filtered_df = filtered_df.filter(pl.col(f"is_{args.type}"))
    
    if args.limit:
        filtered_df = filtered_df.head(args.limit)
    
    print(f"Found {len(filtered_df)} files to process for date {args.date}")
    
    if len(filtered_df) == 0:
        print("No files found for the given criteria.")
        return

    # 4. Download and convert in parallel
    rows = filtered_df.to_dicts()
    with ThreadPoolExecutor(max_workers=8) as executor:
        list(tqdm(executor.map(lambda r: download_and_convert(r, DATA_DIR), rows), total=len(rows), desc="Downloading"))

if __name__ == "__main__":
    main()
