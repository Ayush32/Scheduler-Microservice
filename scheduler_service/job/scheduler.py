from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from .models import Job
from datetime import datetime


scheulder = BackgroundScheduler()

def schedule_job(job_id,job_name,cron_schedule):
    def job_function():
        """
        Function that defines the logic to be executed by the scheduled job.

        Retrieves the job by its ID, performs dummy job logic (e.g., sending email, number crunching),
        updates the last run timestamp of the job, and saves the job.
        """
        # get the job by id
        job = Job.objects.get(id = job_id)
        # Dummy job logic (e.g., send email, number crunching)
        print(f"Executing Job :  {job_name}")
        job.last_run = datetime.now()
        job.save()
    # Convert the cron schedule string into a CronTrigger object
    cron_trigger = CronTrigger.from_crontab(cron_schedule)
    # Add the job function to the scheduler
    scheulder.add_job(job_function,trigger=cron_trigger, id = str(job_id))
    
    

def start_scheduler():
    scheulder.start()
    jobs = Job.objects.all()
    for job in jobs:
        schedule_job(job.id,job.job_name,job.schedule)