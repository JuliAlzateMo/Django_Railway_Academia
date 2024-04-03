# Generated by Django 5.0.3 on 2024-03-23 04:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myAppGestionAcademia', '0029_alter_asistencias_porcentajeasistencia'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='asistencias',
            name='porcentajeAsistencia',
            field=models.IntegerField(blank=True, null=True, verbose_name='%'),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estudiante', models.BooleanField(default=False)),
                ('profesor', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='estudiantes',
            name='fkUsuario',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='myAppGestionAcademia.usuario'),
        ),
        migrations.AddField(
            model_name='profesores',
            name='fkUsuario',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='myAppGestionAcademia.usuario'),
        ),
    ]