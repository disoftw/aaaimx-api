# Generated by Django 3.0.5 on 2021-01-07 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0013_remove_certificate_has_custom_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificate',
            old_name='event',
            new_name='event_title',
        ),
    ]
