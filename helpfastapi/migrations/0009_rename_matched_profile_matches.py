# Generated by Django 4.1.2 on 2022-11-19 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpfastapi', '0008_rename_religion_categories_faith_based_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='matched',
            new_name='matches',
        ),
    ]
