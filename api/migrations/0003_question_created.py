# Generated by Django 2.1.7 on 2019-04-22 17:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190323_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='created',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
