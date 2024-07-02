# Generated by Django 3.2.20 on 2024-04-25 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0004_locationrecording_goingto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dataforlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=100)),
                ('Ambulanceid', models.CharField(max_length=100)),
                ('Hospital', models.CharField(max_length=100)),
                ('Completed', models.BooleanField(default=False)),
            ],
        ),
    ]