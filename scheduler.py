import schedule
import time
import subprocess
import datetime
import sys

def job():
    print(f"[{datetime.datetime.now()}] Starting scheduled job...")
    try:
        # Run the downloader using subprocess
        # Using sys.executable ensures we use the same python interpreter
        result = subprocess.run(
            [sys.executable, "gdelt_downloader.py", "--type", "events"],
            capture_output=True,
            text=True
        )
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
        print(f"[{datetime.datetime.now()}] Job finished.")
    except Exception as e:
        print(f"Error executing job: {e}")

if __name__ == "__main__":
    print("Scheduler started. Running daily at 02:00.")
    
    # Schedule the job every day at 02:00
    schedule.every().day.at("02:00").do(job)
    
    # Also run once on startup to ensure it works (Optional, but good for testing)
    # job() 
    
    while True:
        schedule.run_pending()
        time.sleep(60)
