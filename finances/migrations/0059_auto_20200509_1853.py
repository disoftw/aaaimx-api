# Generated by Django 3.0.5 on 2020-05-09 18:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0058_auto_20200509_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='exp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 10, 18, 53, 19, 94760)),
        ),
    ]
