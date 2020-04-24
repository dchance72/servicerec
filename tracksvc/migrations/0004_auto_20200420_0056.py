# Generated by Django 3.0.3 on 2020-04-20 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracksvc', '0003_auto_20200419_2053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkevent',
            name='loaded',
        ),
        migrations.RemoveField(
            model_name='checkevent',
            name='present',
        ),
        migrations.RemoveField(
            model_name='checkevent',
            name='ready',
        ),
        migrations.AddField(
            model_name='checkevent',
            name='state',
            field=models.IntegerField(choices=[(0, 'Ready'), (1, 'Malfunctioning'), (2, 'Unloaded'), (3, 'Missing'), (4, 'Repair')], default=0),
        ),
    ]