# Generated by Django 4.1.2 on 2022-11-28 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpfastapi', '0001_squashed_0010_alter_profile_matches'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='latitude',
            field=models.FloatField(default=29.6516),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='longitude',
            field=models.FloatField(default=82.3248),
            preserve_default=False,
        ),
    ]
