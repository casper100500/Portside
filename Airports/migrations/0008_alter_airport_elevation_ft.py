# Generated by Django 4.1.2 on 2022-11-10 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Airports', '0007_alter_airport_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='elevation_ft',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]