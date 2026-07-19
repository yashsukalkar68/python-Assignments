import schedule
import time

def job():
    print("Task executed!")

schedule.every(5).seconds.do(job)

print("Scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(1)