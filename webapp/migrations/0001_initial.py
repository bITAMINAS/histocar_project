from django.conf import settings
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('nombre', models.CharField(default='', max_length=20)),
                ('apellido', models.CharField(default='', max_length=20)),
                ('documento', models.CharField(default='', max_length=8, unique=True)),
                ('email', models.EmailField(default='', max_length=254, unique=True)),
                ('telefono', models.CharField(default='', max_length=20)),
                ('tipoUsuario', models.IntegerField(default=0)),
                ('dirDepartamento', models.CharField(default='', max_length=20, verbose_name='Departamento')),
                ('dirCiudad', models.CharField(default='', max_length=20)),
                ('dirCalle', models.CharField(default='', max_length=50)),
                ('dirNumero', models.CharField(default='', max_length=5)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=50)),
                ('descripcion', models.CharField(default='', max_length=240)),
            ],
        ),
        migrations.CreateModel(
            name='EstadoServicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=datetime.datetime(2020, 3, 13, 12, 39, 34, 401340))),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=20)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Marca')),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=240)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, choices=[('Blanco', 'Blanco'), ('Rojo', 'Rojo'), ('Negro', 'Negro'), ('Azul', 'Azul'), ('Bordó', 'Bordó'), ('Marrón', 'Marrón'), ('Gris_Plata', 'Gris Plata'), ('Gris_Ceniza', 'Gris Ceniza'), ('Amarillo', 'Amarillo'), ('Verde', 'Verde'), ('Otro', 'Otro')], max_length=15)),
                ('nroChasis', models.CharField(default='', max_length=50)),
                ('matricula', models.CharField(default='', max_length=50)),
                ('anio', models.IntegerField(default=0)),
                ('tipoCombustible', models.CharField(blank=True, choices=[('Nafta', 'Nafta'), ('Gasoil', 'Gasoil'), ('Híbrido', 'Híbrido'), ('Eléctrico', 'Eléctrico'), ('Hidrógeno', 'Hidrógeno'), ('GLP', 'Glp')], max_length=15)),
                ('duenio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Modelo')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default='10/10/2020 22:22:00')),
                ('textoOtros', models.CharField(default='', max_length=240)),
                ('comentario', models.CharField(default='', max_length=240)),
                ('kilometros', models.IntegerField(default=0)),
                ('puntuacion', models.IntegerField(default=0)),
                ('costo', models.IntegerField(default=0)),
                ('estados', models.ManyToManyField(through='webapp.EstadoServicio', to='webapp.Estado')),
                ('tareas', models.ManyToManyField(to='webapp.Tarea')),
                ('vehiculo', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='webapp.Vehiculo')),
            ],
        ),
        migrations.AddField(
            model_name='estadoservicio',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Servicio'),
        ),
    ]
