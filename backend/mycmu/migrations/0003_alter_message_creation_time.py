# Generated by Django 4.0.3 on 2022-04-16 20:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycmu', '0002_alter_message_creation_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='creation_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 16, 20, 2, 34, 214521)),
        ),
    ]