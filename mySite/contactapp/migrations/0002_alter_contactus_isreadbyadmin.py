# Generated by Django 4.0.6 on 2022-07-27 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='isReadByAdmin',
            field=models.BooleanField(default=False, verbose_name='خوانده شده توسط مدیر'),
        ),
    ]
