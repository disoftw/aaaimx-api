# Generated by Django 2.2.6 on 2019-12-13 17:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0039_auto_20191209_0418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='exp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 12, 14, 17, 52, 15, 698666)),
        ),
    ]