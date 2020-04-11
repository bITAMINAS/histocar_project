# Generated by Django 3.0.4 on 2020-03-25 02:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20200315_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='is_client',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='estadoservicio',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 23, 13, 1, 694609)),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='anio',
            field=models.IntegerField(default=2020),
        ),
    ]
