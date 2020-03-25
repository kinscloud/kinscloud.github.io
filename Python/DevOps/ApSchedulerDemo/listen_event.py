from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
import datetime
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt=' %Y-%m-%d %H:%m:%S',
                    filename='./log1.log',
                    filemode='a')


def aps_test(x):
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%m:%S"), x)


def date_test(x):
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%m:%S"), x)
    print(1/0)


def my_listener(event):
    if event.exception:
        print('error....')
    else:
        print('running....')


scheduler = BlockingScheduler()
scheduler.add_job(func=date_test, args=('have error',),
                  next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=15), id='date_task')
scheduler.add_job(func=aps_test, args=('loop task',),
                  trigger='interval', seconds=3, id='interval_task')
scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
scheduler._logger = logging

scheduler.start()
