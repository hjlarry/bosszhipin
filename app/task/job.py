from ..task import celery_app
from ..util.SpiderWorker import SpiderWorker
from common import constants
from ..util.Log import other_log


@celery_app.task(ignore_result=True)
def job_task():
    for career in SpiderWorker().career_spider():
        urls = [constants.HOME_URL + career + '?page={}&ka=page-{}'.format(page, page) for page in range(1, 31)]
        for url in urls:
            celery_app.send_task('app.task.job.get_job', args=(url,), queue='get_job_list', routing_key='get_job_list')


@celery_app.task(ignore_result=True)
def job_task_from_city():
    for city in SpiderWorker().city_spider(update_db=False):
        urls = [constants.HOME_URL+'/c'+city['city_id']+'/h_100010000/?page={}&ka=page-{}'.format(page, page) for page in range(1, 31)]
        for url in urls:
            celery_app.send_task('app.task.job.get_job', args=(url,), queue='get_job_list', routing_key='get_job_list')



@celery_app.task(ignore_result=True)
def get_job(url):
    SpiderWorker(url).job_spider()


@celery_app.task(ignore_result=True)
def job_des_task(times=10):
    for i in range(times):
        celery_app.send_task('app.task.job.get_job_des', queue='other_queue', routing_key='other_queue')


@celery_app.task(ignore_result=True)
def get_job_des():
    SpiderWorker().job_des_spider()


if __name__ == '__main__':
    job_task()
    # job_des_task()