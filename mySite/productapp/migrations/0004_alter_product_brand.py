# Generated by Django 4.0.6 on 2022-07-26 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0003_productbrand_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='productapp.productbrand', verbose_name='برند'),
        ),
    ]
