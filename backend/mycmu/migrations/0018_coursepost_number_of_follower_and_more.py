# Generated by Django 4.0.3 on 2022-04-22 13:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycmu', '0017_alter_message_creation_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursepost',
            name='number_of_follower',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='creation_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 22, 13, 55, 58, 341963)),
        ),
    ]
