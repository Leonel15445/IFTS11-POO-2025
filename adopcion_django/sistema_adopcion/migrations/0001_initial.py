# Generated by Django 5.2.3 on 2025-06-25 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('raza', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('tamaño', models.CharField(max_length=20)),
                ('peso', models.FloatField()),
                ('estado_salud', models.CharField(max_length=100)),
                ('vacunado', models.BooleanField()),
                ('estado', models.CharField(choices=[('disponible', 'Disponible'), ('reservado', 'Reservado'), ('adoptado', 'Adoptado')], max_length=20)),
                ('temperamento', models.CharField(max_length=100)),
            ],
        ),
    ]
