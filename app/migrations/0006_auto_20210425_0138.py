# Generated by Django 3.2 on 2021-04-24 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_regiondimensionandcoordinates_schedule_singlelinetextmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='regiondimensionandcoordinates',
            name='type',
            field=models.CharField(default='single', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schedule',
            name='type',
            field=models.CharField(default='single', max_length=200),
            preserve_default=False,
        ),
    ]