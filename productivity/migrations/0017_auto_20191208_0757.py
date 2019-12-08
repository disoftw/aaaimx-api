# Generated by Django 2.2.6 on 2019-12-08 07:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productivity', '0016_auto_20191208_0226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='membership',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='photo',
        ),
        migrations.AddField(
            model_name='membership',
            name='member',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='productivity.Member'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='exp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 12, 9, 7, 56, 55, 933879)),
        ),
    ]
