# Generated by Django 3.0.4 on 2020-03-15 02:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20200314_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estadoservicio',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 14, 23, 9, 19, 953034)),
        ),
    ]
