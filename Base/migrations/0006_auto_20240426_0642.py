# Generated by Django 3.2.20 on 2024-04-26 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0005_dataforlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataforlist',
            name='HospLattitude',
            field=models.FloatField(default=12.34),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dataforlist',
            name='HospLongitude',
            field=models.FloatField(default=12.34),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dataforlist',
            name='Lattitude',
            field=models.FloatField(default=234.435),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dataforlist',
            name='Longitude',
            field=models.FloatField(default=2432.23),
            preserve_default=False,
        ),
    ]
