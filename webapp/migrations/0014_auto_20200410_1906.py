# Generated by Django 3.0.4 on 2020-04-10 22:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_auto_20200409_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estadoservicio',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 19, 6, 48, 626525)),
        ),
    ]
