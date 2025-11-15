from app.core.celery import celery_app

@celery_app.task(name="demo.ping")
def ping():
    return "pong"
