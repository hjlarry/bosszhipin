from ..util.SpiderWorker import SpiderWorker
from ..task import celery_app


@celery_app.task(ignore_result=True)
def get_city():
    SpiderWorker().city_spider()


@celery_app.task(ignore_result=True)
def city_task():
    celery_app.send_task('app.task.city.get_city', queue='get_job_list', routing_key='get_job_list')