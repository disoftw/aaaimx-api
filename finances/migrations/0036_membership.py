# Generated by Django 2.2.6 on 2019-12-08 22:41

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('productivity', '0022_auto_20191208_2158'),
        ('finances', '0035_delete_membership'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('QR', models.URLField(blank=True, default='', max_length=100)),
                ('exp', models.DateTimeField(blank=True, default=datetime.datetime(2019, 12, 9, 22, 41, 6, 800567))),
                ('income', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='finances.BankMovement')),
                ('member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='productivity.Member')),
            ],
        ),
    ]
