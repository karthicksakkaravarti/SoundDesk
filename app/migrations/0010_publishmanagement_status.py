# Generated by Django 3.2 on 2021-04-25 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_publishmanagement'),
    ]

    operations = [
        migrations.AddField(
            model_name='publishmanagement',
            name='status',
            field=models.CharField(default='Saved', max_length=200),
            preserve_default=False,
        ),
    ]