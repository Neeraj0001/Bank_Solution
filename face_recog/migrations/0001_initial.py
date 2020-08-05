# Generated by Django 3.0.8 on 2020-08-01 04:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('age', models.IntegerField(null=True)),
                ('Experience', models.CharField(max_length=200, null=True)),
                ('country', models.CharField(max_length=200, null=True)),
                ('location', models.CharField(max_length=200, null=True)),
                ('Email', models.CharField(max_length=200, null=True)),
                ('Phone', models.CharField(max_length=200, null=True)),
                ('Internship', models.CharField(max_length=200, null=True)),
                ('Bio', models.CharField(max_length=1000, null=True)),
                ('skill_1', models.CharField(max_length=200, null=True)),
                ('skill_2', models.CharField(max_length=200, null=True)),
                ('skill_3', models.CharField(max_length=200, null=True)),
                ('profile_pics', models.ImageField(blank=True, default='unknown.png', null=True, upload_to='')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]