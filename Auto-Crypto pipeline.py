import schedule
import time
import os

# 🧠 Define the job to run
def run_etl():
    print("🚀 Running ETL Pipeline...")
    os.system('python "C:/Users/Sober/OneDrive/Desktop/API DATA ENGINEERING/Webscraping.py"')
    print("✅ ETL job completed.")

# ⏰ Schedule it: every day at 7:51 PM
schedule.every().day.at("06:00").do(run_etl)

print("📅 Scheduler started. Waiting for job time...")

# 🔁 Keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)














































































































































































