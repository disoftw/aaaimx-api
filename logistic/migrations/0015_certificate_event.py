# Generated by Django 3.0.5 on 2021-01-07 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0014_auto_20210107_0626'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='logistic.Event'),
        ),
    ]
