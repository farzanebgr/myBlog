# Generated by Django 4.0.6 on 2022-07-28 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='تصویر آواتار'),
        ),
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='تلفن همراه'),
        ),
    ]