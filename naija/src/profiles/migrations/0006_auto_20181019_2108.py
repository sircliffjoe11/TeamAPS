# Generated by Django 2.1.2 on 2018-10-19 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_profile_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Location',
            field=models.CharField(blank=True, default='my location default', max_length=20, null=True),
        ),
    ]
