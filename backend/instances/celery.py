from celery import Celery

celeryservice = Celery('asynchronous tasks')
# , broker='redis://127.0.0.1:6379', backend='redis://127.0.0.1:6379'