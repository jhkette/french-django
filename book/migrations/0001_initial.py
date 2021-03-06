# Generated by Django 3.0.6 on 2020-05-21 17:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vocabulary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('author', models.CharField(max_length=200)),
                ('date_published', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('vocabulary', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='vocabulary.Vocabulary')),
            ],
        ),
    ]
