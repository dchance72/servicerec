# Generated by Django 3.0.3 on 2020-04-18 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Firearm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=32)),
                ('model', models.CharField(max_length=32)),
                ('serial', models.CharField(max_length=32)),
            ],
            options={
                'ordering': ['make'],
            },
        ),
    ]
