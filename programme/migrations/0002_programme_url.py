# Generated by Django 3.0.6 on 2020-05-22 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programme', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='programme',
            name='url',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
