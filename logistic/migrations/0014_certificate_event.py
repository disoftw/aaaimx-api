# Generated by Django 3.0.5 on 2020-06-09 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0013_auto_20200609_0331'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='event',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]