# Generated by Django 4.0.3 on 2022-04-19 21:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycmu', '0013_remove_profile_full_name_remove_profile_user_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='creation_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 19, 21, 7, 4, 574132)),
        ),
    ]