# Generated by Django 2.1.2 on 2018-10-19 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profiles_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(default='description default text')),
            ],
        ),
        migrations.DeleteModel(
            name='profiles',
        ),
    ]