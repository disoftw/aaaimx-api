# Generated by Django 2.2.6 on 2019-11-21 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productivity', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='research',
            old_name='published_in',
            new_name='pub_in',
        ),
        migrations.AddField(
            model_name='research',
            name='pub_type',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]