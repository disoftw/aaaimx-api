# Generated by Django 2.2.6 on 2019-11-24 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productivity', '0003_auto_20191121_0632'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advisor',
            old_name='thesis',
            new_name='research',
        ),
    ]
