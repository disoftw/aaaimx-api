# Generated by Django 2.2.6 on 2020-01-27 15:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0047_auto_20200124_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='exp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 1, 28, 15, 56, 56, 548223)),
        ),
    ]
