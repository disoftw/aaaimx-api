# Generated by Django 3.0.5 on 2020-06-13 20:10

import datetime
from django.db import migrations, models
import django.db.models.deletion
import gdstorage.storage
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, unique=True)),
                ('story', models.TextField(blank=True, default='')),
                ('logo', models.ImageField(blank=True, default=None, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='logos')),
            ],
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(default='', max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('surname', models.CharField(blank=True, default='', max_length=100)),
                ('email', models.EmailField(blank=True, default='', max_length=100)),
                ('active', models.BooleanField(default=False)),
                ('board', models.BooleanField(blank=True, default=False)),
                ('committee', models.BooleanField(blank=True, default=False)),
                ('thumbnailFile', models.ImageField(blank=True, default=None, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='thumbnail')),
                ('charge', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=255, unique=True)),
                ('alias', models.CharField(blank=True, max_length=100)),
                ('site', models.URLField(blank=True, default='', max_length=100)),
                ('logoName', models.CharField(blank=True, max_length=100)),
                ('logoFile', models.ImageField(blank=True, default=None, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='logos')),
                ('type', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, default='')),
                ('start', models.DateField(blank=True, default=datetime.datetime.now)),
                ('end', models.DateField(blank=True, default=datetime.datetime.now)),
                ('responsible', models.CharField(blank=True, default='', max_length=100)),
                ('collaborators', models.ManyToManyField(blank=True, to='productivity.Member', verbose_name='collaborators')),
                ('institute', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='productivity.Partner')),
                ('lines', models.ManyToManyField(blank=True, to='productivity.Line', verbose_name='interest areas')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Research',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.TextField(default='')),
                ('resume', models.TextField(blank=True, default='')),
                ('year', models.IntegerField(blank=True, default=2018)),
                ('grade', models.CharField(blank=True, default='', max_length=100)),
                ('event', models.CharField(blank=True, default='', max_length=200)),
                ('pub_in', models.CharField(blank=True, default='', max_length=200)),
                ('pub_type', models.CharField(blank=True, default='', max_length=200)),
                ('type', models.CharField(blank=True, default='', max_length=200)),
                ('link', models.URLField(blank=True, default='', max_length=500)),
                ('lines', models.ManyToManyField(blank=True, to='productivity.Line', verbose_name='research lines')),
                ('projects', models.ManyToManyField(blank=True, to='productivity.Project', verbose_name='related projects')),
            ],
            options={
                'verbose_name_plural': 'research',
            },
        ),
        migrations.AddField(
            model_name='member',
            name='adscription',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='adscription_institute', to='productivity.Partner'),
        ),
        migrations.AddField(
            model_name='member',
            name='divisions',
            field=models.ManyToManyField(blank=True, to='productivity.Division', verbose_name='members'),
        ),
        migrations.AddField(
            model_name='member',
            name='roles',
            field=models.ManyToManyField(blank=True, to='productivity.Role', verbose_name='list of roles'),
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(blank=True, default=1)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productivity.Member')),
                ('research', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='productivity.Research')),
            ],
        ),
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(blank=True, default=1)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productivity.Member')),
                ('research', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advisors', to='productivity.Research')),
            ],
        ),
    ]
