# Generated by Django 4.1.2 on 2022-11-08 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Airports', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AirportModel',
            new_name='Airport',
        ),
    ]
