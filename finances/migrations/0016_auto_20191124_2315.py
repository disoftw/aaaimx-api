# Generated by Django 2.2.6 on 2019-11-24 23:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0015_auto_20191124_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='exp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 25, 23, 15, 32, 724305)),
        ),
    ]
