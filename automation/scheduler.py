import schedule
import time

def run_scheduler(job):

    schedule.every(1).hours.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)