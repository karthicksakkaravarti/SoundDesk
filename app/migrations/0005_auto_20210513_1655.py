# Generated by Django 3.2 on 2021-05-13 11:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_vmds_vmdstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publishmanagement',
            name='Duration',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='publishmanagement',
            name='RepeatCount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='publishmanagement',
            name='StartDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='publishmanagement',
            name='StartTime',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='publishmanagement',
            name='status',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='publishmanagement',
            name='type',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='publishmanagement',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
