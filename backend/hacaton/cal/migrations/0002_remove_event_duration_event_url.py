# Generated by Django 5.0.4 on 2024-04-06 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='duration',
        ),
        migrations.AddField(
            model_name='event',
            name='url',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
