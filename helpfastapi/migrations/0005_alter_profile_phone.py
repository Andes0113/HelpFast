# Generated by Django 4.1.2 on 2022-11-08 23:01

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('helpfastapi', '0004_alter_profile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, max_length=31, null=True),
        ),
    ]
