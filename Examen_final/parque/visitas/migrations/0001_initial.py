# Generated by Django 3.1.3 on 2020-11-14 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='origen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='visita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Apellido', models.CharField(max_length=50)),
                ('Edad', models.IntegerField()),
                ('Sexo', models.CharField(max_length=1)),
                ('Pais', models.CharField(max_length=50, verbose_name='País o Departamento')),
                ('Documento', models.CharField(max_length=50, verbose_name='Pasaporte o DPI')),
                ('Fecha', models.DateField(verbose_name='Fecha de visita')),
                ('Tarifa', models.FloatField()),
                ('Origen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitas.origen')),
            ],
        ),
        migrations.CreateModel(
            name='actividades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activiti', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitas.activity')),
                ('visitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitas.visita')),
            ],
        ),
    ]
