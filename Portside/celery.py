import os
from celery import Celery
from celery.schedules import crontab
#from Airports.tasks import task_bulk_create_update

os.environ.setdefault('DJANGO_SETTINGS_MODULE','Portside.settings')

app = Celery('fetch_csv_to_model')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks() 

#beat doesn't work on Windows 10
app.conf.beat_schedule={
    'run-download-update-every-5-minute':{
        'task':'Airports.tasks.task_bulk_create_update',
        'args': ['url'], #default type='url' if there is no Internet then type='file'...
        #'schedule': 60.0
        'schedule':crontab(minute='*/10'),
    },
}

# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # Calls test('hello') every 10 seconds.
#     sender.add_periodic_task(10.0, task_bulk_create_update('file'), name='add every 10')