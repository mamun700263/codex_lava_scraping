from celery import Celery

celery_app = Celery(
    "playwrite_tasks",
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/0",
    include=["app.tasks"]
)

celery_app.conf.broker_url = "redis://127.0.0.1:6379/0"
celery_app.conf.result_backend = "redis://127.0.0.1:6379/0"

celery_app.autodiscover_tasks(["app.tasks"])
