# Generated by Django 4.1.2 on 2022-11-06 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpfastapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='matched',
            field=models.ManyToManyField(blank=True, related_name='matched', to='helpfastapi.organization'),
        ),
        migrations.AlterField(
            model_name='user',
            name='seen',
            field=models.ManyToManyField(blank=True, related_name='seen', to='helpfastapi.organization'),
        ),
    ]
