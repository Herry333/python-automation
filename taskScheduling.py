import schedule
import time

def job():
    print( "job is executed")

schedule.every().day.at("19:43").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)





