# Generated by Django 3.0.3 on 2020-04-23 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracksvc', '0006_auto_20200423_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkevent',
            name='state',
            field=models.IntegerField(choices=[(0, 'Ready'), (1, 'Malfunctioning'), (2, 'Not loaded'), (3, 'Not In Service'), (4, 'In for Repair'), (5, 'Non-functional'), (6, 'Decommissioned')], default=0),
        ),
    ]
