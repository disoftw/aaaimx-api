# Generated by Django 3.0.5 on 2020-06-09 03:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0061_auto_20200509_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='exp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 10, 3, 28, 27, 664489)),
        ),
    ]
