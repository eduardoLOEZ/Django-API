# Generated by Django 4.2.3 on 2023-07-09 02:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=datetime.datetime(2022, 1, 1, 0, 0)
            ),
            preserve_default=False,
        ),
    ]
