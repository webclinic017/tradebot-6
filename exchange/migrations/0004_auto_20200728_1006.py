# Generated by Django 3.0.8 on 2020-07-28 07:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0003_exchange_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchange',
            name='date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]