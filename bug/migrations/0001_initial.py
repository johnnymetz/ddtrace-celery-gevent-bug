# Generated by Django 4.1.7 on 2023-03-23 17:20

import bug.storage_backends
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FileObject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        storage=bug.storage_backends.FileStorage(), upload_to=""
                    ),
                ),
            ],
        ),
    ]
