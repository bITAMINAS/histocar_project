# Generated by Django 3.0.4 on 2020-03-29 21:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_auto_20200328_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estadoservicio',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 29, 18, 41, 33, 458784)),
        ),
    ]
