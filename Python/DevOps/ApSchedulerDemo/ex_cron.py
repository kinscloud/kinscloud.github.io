#encoding=utf-8
from datetime import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler

def tick():
    print('Tick! The time is: %s' % datetime.now())
    
if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(tick, 'cron',hour=15,minute=21)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    
    try:
        scheduler.start()
    except (KeyboardInterrupt,SystemExit):
        pass