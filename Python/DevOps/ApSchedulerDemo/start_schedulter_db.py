from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore


def my_job(id='my_job'):
    print(id, '-->', datetime.datetime.now())


jobstores = {
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqllite')
}

executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(10)
}

job_defaults = {
    'coalesce': False,
    'max_instances': 3
}

scheduler = BlockingScheduler(
    jobstores=jobstores, executors=executors, job_defaults=job_defaults)
scheduler.add_job(my_job, args=['job_interval', ], id='job_interval',
                  trigger='interval', seconds=5, replace_existing=True)
# scheduler.add_job(my_job, args=['job_cron', ], id='job_cron', trigger='cron',
#                   month='3-6,11-12', hour='13-18', second='*/10', end_date='2020-3-31')
scheduler.add_job(my_job, args=['job_cron', ], id='job_cron', trigger='cron',
                  month='3-6,11-12', hour='13-18', second='*/10', coalesce=True,
                  misfire_grace_time=30, replace_existing=True, end_date='2020-3-31')
scheduler.add_job(my_job, args=['job_once_now', ], id='job_once_now')
scheduler.add_job(my_job, args=['job_date_once', ], id='job_date_once',
                  trigger='date', run_date='2020-3-25 15:48:00')
try:
    scheduler.start()
except SystemExit:
    print('exit')
    exit()


# scheduler.remove_job(job_id,jobstore=None)
# scheduler.remove_all_jobs(jobstore=None)
# scheduler.pause_job(job_id,jobstore=None)
# scheduler.resume_job()(job_id,jobstore=None)
# scheduler.modify_job(job_id,jobstore=None,**changes)
# scheduler.reschedule_job(job_id,jobstore=None,trigger=None,**trigger_args)
# scheduler.print_jobs(jobstore=None,out=sys.stdout)