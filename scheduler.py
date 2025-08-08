from apscheduler.schedulers.blocking import BlockingScheduler
from fetch_weather import fetch_weather
from load_to_db import load_to_db

def job():
    weather_data = fetch_weather()
    load_to_db(weather_data)
    print("Weerdata opgehaald en opgeslagen")

if __name__ == "__main__":
    scheduler = BlockingScheduler()
    # PLan de job om elk uur te draaien, op minuut 0
    scheduler.add_job(job, 'cron', minute=0)
    print("Scheduler gestart, job draait elk uur op minuut 0")
    scheduler.start()