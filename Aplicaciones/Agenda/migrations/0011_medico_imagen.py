# Generated by Django 3.1.7 on 2021-04-07 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agenda', '0010_medico_nombre_apellido'),
    ]

    operations = [
        migrations.AddField(
            model_name='medico',
            name='imagen',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
