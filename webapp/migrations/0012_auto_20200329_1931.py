# Generated by Django 3.0.4 on 2020-03-29 22:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_auto_20200329_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estadoservicio',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 29, 19, 31, 28, 205001)),
        ),
    ]
