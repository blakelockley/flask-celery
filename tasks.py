from celery import Celery
from time import sleep

app = Celery("tasks", backend='redis://localhost', broker="redis://localhost")


@app.task
def add_task(x, y):
    sleep(5)
    return x + y
