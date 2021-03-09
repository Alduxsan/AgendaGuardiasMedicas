# Generated by Django 2.2.6 on 2020-03-09 00:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Agenda', '0004_auto_20200308_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL),
        ),
    ]