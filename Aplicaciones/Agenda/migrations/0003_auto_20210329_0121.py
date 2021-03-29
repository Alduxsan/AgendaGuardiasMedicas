# Generated by Django 3.1.7 on 2021-03-29 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Agenda', '0002_auto_20210327_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='guardia',
            name='departamento',
            field=models.CharField(default='Sin asignar', max_length=20),
        ),
        migrations.AlterField(
            model_name='guardia',
            name='medico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Agenda.medico'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='ranking',
            field=models.IntegerField(),
        ),
    ]
