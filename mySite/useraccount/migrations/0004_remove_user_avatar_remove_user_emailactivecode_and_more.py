# Generated by Django 4.0.6 on 2022-07-29 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0003_user_age_user_gender_user_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='user',
            name='emailActiveCode',
        ),
        migrations.RemoveField(
            model_name='user',
            name='mobile',
        ),
    ]
