# Generated by Django 3.0.4 on 2020-04-17 01:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0015_auto_20200415_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='media/avatar'),
        ),
        migrations.AlterField(
            model_name='estadoservicio',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 16, 22, 14, 47, 821980)),
        ),
    ]
