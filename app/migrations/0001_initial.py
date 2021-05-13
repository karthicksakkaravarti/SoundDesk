# Generated by Django 3.2 on 2021-05-01 08:12

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(blank=True, max_length=500)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlistname', models.CharField(max_length=200)),
                ('XCoOrdinates', models.IntegerField()),
                ('YCoOrdinates', models.IntegerField()),
                ('Width', models.IntegerField()),
                ('Height', models.IntegerField()),
                ('BorderLine', models.CharField(max_length=200)),
                ('BackGroundColor', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('singleLineMessage', models.TextField(blank=True, null=True)),
                ('multilineMessage', models.TextField(blank=True, null=True)),
                ('imageMessage', models.FileField(blank=True, null=True, upload_to='')),
                ('videoMessage', models.FileField(blank=True, null=True, upload_to='')),
                ('CreatedDate', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RegionDimensionAndCoOrdinates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('XCoOrdinates', models.IntegerField()),
                ('YCoOrdinates', models.IntegerField()),
                ('Width', models.IntegerField()),
                ('Height', models.IntegerField()),
                ('BorderLine', models.CharField(max_length=200)),
                ('BackGroundColor', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StartDate', models.DateField()),
                ('StartTime', models.TimeField()),
                ('Duration', models.CharField(max_length=100)),
                ('RepeatCount', models.IntegerField()),
                ('type', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VMDS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VMDName', models.CharField(max_length=200)),
                ('VMDLocation', models.CharField(max_length=200)),
                ('VMDLatitude', models.CharField(max_length=200)),
                ('VMDLongitude', models.CharField(max_length=200)),
                ('VMDIPAddress', models.GenericIPAddressField(verbose_name='IP Address')),
                ('VMDPort', models.IntegerField()),
                ('VMDResolutionHeight', models.IntegerField()),
                ('VMDResolutionwidth', models.IntegerField()),
                ('VMDStatus', models.CharField(max_length=200)),
                ('VMDBrightness', models.IntegerField()),
                ('AssigneUser', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='VMDGroups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GroupName', models.CharField(max_length=300)),
                ('CreatedBy', models.CharField(max_length=300)),
                ('CreatedDate', models.DateTimeField(auto_now=True)),
                ('VMDS', models.ManyToManyField(to='app.VMDS')),
            ],
        ),
        migrations.CreateModel(
            name='VMDConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ON_OFF_Scheduling', models.BooleanField()),
                ('VMD_Brightness', models.BooleanField()),
                ('Resolution', models.BooleanField()),
                ('wakeUptime', models.TimeField(blank=True, null=True)),
                ('Sleeptime', models.TimeField(blank=True, null=True)),
                ('Reboottime', models.TimeField(blank=True, null=True)),
                ('Brightness', models.IntegerField(blank=True, null=True)),
                ('width', models.IntegerField(blank=True, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('VMDS', models.ManyToManyField(to='app.VMDS')),
            ],
        ),
        migrations.CreateModel(
            name='TextMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('video', models.FileField(blank=True, null=True, upload_to='')),
                ('type', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('RegionDimensionAndCoOrdinates', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.regiondimensionandcoordinates')),
                ('Schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.schedule')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PublishManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StartDate', models.DateField()),
                ('StartTime', models.TimeField()),
                ('Duration', models.CharField(max_length=100)),
                ('RepeatCount', models.IntegerField()),
                ('type', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('CreatedDate', models.DateTimeField(auto_now=True)),
                ('playlist', models.ManyToManyField(to='app.Playlist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vmd', models.ManyToManyField(blank=True, null=True, to='app.VMDS')),
                ('vmdGroups', models.ManyToManyField(blank=True, null=True, to='app.VMDGroups')),
            ],
        ),
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('operation', models.ManyToManyField(to='app.Operation')),
            ],
        ),
        migrations.CreateModel(
            name='DeveiceGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('device', models.ManyToManyField(to='app.Devices')),
            ],
        ),
    ]
