# Generated by Django 4.1.7 on 2023-03-10 12:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("BlogApp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="home",
            name="d2",
            field=models.TextField(default=datetime.time(0, 0), max_length=50000),
            preserve_default=False,
        ),
    ]