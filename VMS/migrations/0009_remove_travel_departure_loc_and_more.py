# Generated by Django 4.0.2 on 2022-02-24 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VMS', '0008_alter_driverdoc_marritial_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='travel',
            name='departure_loc',
        ),
        migrations.RemoveField(
            model_name='travel',
            name='departure_time',
        ),
        migrations.RemoveField(
            model_name='travel',
            name='location',
        ),
        migrations.RemoveField(
            model_name='travel',
            name='routes',
        ),
    ]
