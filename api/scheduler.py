from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import guardia_ranking_update

def start_jobs():
    scheduler = BackgroundScheduler()
    
    #Set cron to runs every 1 min.
    cron_job = {'month': '*', 'day': '*', 'hour': '*', 'minute':'*/1'}
    
    #Add our task to scheduler.
    scheduler.add_job(guardia_ranking_update, 'cron', **cron_job)
#And finally start.    
    #scheduler.start()
