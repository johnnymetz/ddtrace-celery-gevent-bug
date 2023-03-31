from django.core.files.base import ContentFile
from django.utils import timezone

from bug.models import FileObject
from mysite.celery import app


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")


@app.task(bind=True)
def upload_file_to_s3(self):
    obj = FileObject()
    obj.file.save("file.txt", ContentFile("Hello world"))
