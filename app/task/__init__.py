from celery import Celery


tasks = ['app.task.city', 'app.task.company', 'app.task.job']
celery_app = Celery('tasks', include=tasks)
celery_app.config_from_object('app.task.celery_config')