# Generated by Django 4.1.2 on 2022-12-03 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpfastapi', '0015_alter_organization_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='address',
            field=models.CharField(max_length=100),
        ),
    ]
