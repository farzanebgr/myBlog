# Generated by Django 4.0.6 on 2022-07-28 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0004_alter_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/products', verbose_name='تصویر محصول'),
        ),
    ]
