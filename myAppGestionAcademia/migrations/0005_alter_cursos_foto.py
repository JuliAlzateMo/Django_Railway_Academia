# Generated by Django 5.0.3 on 2024-03-13 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myAppGestionAcademia', '0004_alter_cursos_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='foto',
            field=models.ImageField(default=None, upload_to='foto'),
        ),
    ]
