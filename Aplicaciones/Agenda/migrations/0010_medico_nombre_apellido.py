# Generated by Django 3.1.7 on 2021-04-05 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agenda', '0009_auto_20210401_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='medico',
            name='Nombre_Apellido',
            field=models.CharField(default='QuimeraDevs', max_length=30),
        ),
    ]
