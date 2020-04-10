# Generated by Django 3.0.4 on 2020-04-09 21:29

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_auto_20200403_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado',
            name='descripcion',
            field=models.CharField(default='', max_length=240, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='estadoservicio',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 9, 18, 29, 47, 839165)),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='kilometros',
            field=models.IntegerField(default=0, verbose_name='Kilómetros'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='puntuacion',
            field=models.IntegerField(default=0, verbose_name='Calificación'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='textoOtros',
            field=models.TextField(blank=True, default='', max_length=240, verbose_name='Otras tareas'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='dirCalle',
            field=models.CharField(default='', max_length=50, verbose_name='Calle'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='dirCiudad',
            field=models.CharField(default='', max_length=20, verbose_name='Ciudad'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='dirNumero',
            field=models.CharField(default='', max_length=5, verbose_name='Número'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='is_client',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(default='', max_length=20, verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipoUsuario',
            field=models.IntegerField(default=1, verbose_name='Tipo de usuario'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='anio',
            field=models.IntegerField(default=2020, verbose_name='Año'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='duenio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Propietario'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='matricula',
            field=models.CharField(default='', max_length=50, verbose_name='Matrícula'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='nroChasis',
            field=models.CharField(default='', max_length=50, verbose_name='Número de chasis'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='tipoCombustible',
            field=models.CharField(blank=True, choices=[('Nafta', 'Nafta'), ('Gasoil', 'Gasoil'), ('Híbrido', 'Híbrido'), ('Eléctrico', 'Eléctrico'), ('Hidrógeno', 'Hidrógeno'), ('GLP', 'Glp')], max_length=15, verbose_name='Tipo de combustible'),
        ),
    ]
