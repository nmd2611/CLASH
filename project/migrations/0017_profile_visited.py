# Generated by Django 2.2.3 on 2019-08-28 14:36

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0016_remove_profile_visited'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='visited',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0, null=True), null=True, size=100),
        ),
    ]
