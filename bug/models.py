from django.db import models

from bug.storage_backends import FileStorage


class FileObject(models.Model):
    file = models.FileField(storage=FileStorage())

    def __str__(self):
        return self.file.name
