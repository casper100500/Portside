from Portside.celery import app

from .service import csvFileToModel

@app.task
def task_bulk_create_update(type):
    csvFileToModel(type)