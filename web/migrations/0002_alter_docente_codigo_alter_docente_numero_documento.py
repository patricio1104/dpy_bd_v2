# Generated by Django 4.2 on 2023-10-20 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docente',
            name='codigo',
            field=models.CharField(blank=True, max_length=8, verbose_name='Codigo'),
        ),
        migrations.AlterField(
            model_name='docente',
            name='numero_documento',
            field=models.CharField(blank=True, max_length=10, verbose_name='Numero de documento'),
        ),
    ]
