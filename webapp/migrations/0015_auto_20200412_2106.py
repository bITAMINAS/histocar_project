# Generated by Django 3.0.4 on 2020-04-13 00:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_auto_20200410_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estadoservicio',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 12, 21, 6, 40, 813347)),
        ),
    ]
