# Generated by Django 3.0.8 on 2020-07-28 06:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exchange',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='exchange',
            name='url',
            field=models.CharField(max_length=255),
        ),
    ]
