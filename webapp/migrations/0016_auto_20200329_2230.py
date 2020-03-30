# Generated by Django 3.0.4 on 2020-03-30 01:30

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0015_auto_20200329_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estadoservicio',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 29, 22, 30, 20, 360815)),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='duenio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
