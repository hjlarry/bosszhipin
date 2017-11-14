from ..util.SpiderWorker import SpiderWorker
from ..task import celery_app


@celery_app.task(ignore_result=True)
def get_company():
    SpiderWorker().company_spider()


@celery_app.task(ignore_result=True)
def company_task(times=10):
    for i in range(times):
        celery_app.send_task('app.task.company.get_company', queue='other_queue', routing_key='other_queue')