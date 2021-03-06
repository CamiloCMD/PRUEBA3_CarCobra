# Generated by Django 3.2.4 on 2021-06-16 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.CharField(max_length=17)),
                ('patente', models.CharField(max_length=6)),
                ('anioFabricacion', models.IntegerField(max_length=4)),
                ('fechaRecepcion', models.DateTimeField(blank=True, null=True)),
                ('marca', models.CharField(max_length=25)),
                ('modelo', models.CharField(max_length=25)),
            ],
        ),
    ]
