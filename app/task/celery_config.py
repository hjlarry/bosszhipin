from common.config import REDIS_CONF
from kombu import Queue, Exchange
from datetime import timedelta


BROKER_URL = 'redis://:{}@{}:{}/{}'.format(REDIS_CONF['password'], REDIS_CONF['host'], REDIS_CONF['port'], REDIS_CONF['broker_db'])
CELERY_RESULT_BACKEND = 'redis://:{}@{}:{}/{}'.format(REDIS_CONF['password'], REDIS_CONF['host'], REDIS_CONF['port'], REDIS_CONF['backend_db'])
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_ENABLE_UTC = True
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 4
CELERY_ACCEPT_CONTENT = ['json']
CELERY_QUEUES=(
        Queue('get_job_list', exchange=Exchange('get_job_list', type='direct'), routing_key='get_job_list'),
        Queue('other_queue', exchange=Exchange('other_queue', type='direct'), routing_key='other_queue'),
)

CELERYBEAT_SCHEDULE={
    'get_job': {
        'task': 'app.task.job.job_task',
        'schedule': timedelta(hours=48),
        'options': {'queue': 'get_job_list', 'routing_key': 'get_job_list'}
    },
    'update_city': {
        'task':'app.task.city.city_task',
        'schedule': timedelta(days=10),
        'options': {'queue': 'get_job_list', 'routing_key': 'get_job_list'}
    }
}