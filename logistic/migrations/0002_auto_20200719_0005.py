# Generated by Django 3.0.5 on 2020-07-19 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to='certs'),
        ),
    ]
