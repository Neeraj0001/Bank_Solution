# Generated by Django 3.0.8 on 2020-08-01 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face_recog', '0004_profile_exp_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='cvv',
        ),
        migrations.AlterField(
            model_name='profile',
            name='Exp_Date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
