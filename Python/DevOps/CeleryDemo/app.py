from __future__ import absolute_import

from celery import Celery

app = Celery("CeleryDemo",include=["CeleryDemo.tasks"])

app.config_from_object("CeleryDemo.settings")

if __name__ == "__main__":
    app.start()