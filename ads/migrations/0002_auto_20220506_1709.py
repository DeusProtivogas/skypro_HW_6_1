# Generated by Django 2.2.12 on 2022-05-06 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ad',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
