# Generated by Django 3.2.20 on 2024-04-24 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0005_hospitals_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitals',
            name='logo',
            field=models.CharField(max_length=300),
        ),
    ]