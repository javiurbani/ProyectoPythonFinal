# Generated by Django 4.1 on 2022-10-06 19:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AppMascota', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
