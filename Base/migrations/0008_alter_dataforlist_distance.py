# Generated by Django 3.2.20 on 2024-04-28 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0007_dataforlist_distance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataforlist',
            name='distance',
            field=models.CharField(default='0.0', max_length=15),
        ),
    ]
