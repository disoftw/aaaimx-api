# Generated by Django 2.2.6 on 2019-11-16 23:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0005_auto_20191116_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='exp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 17, 23, 36, 3, 706111)),
        ),
    ]
