# Generated by Django 4.0.6 on 2022-07-25 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='نام')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('shortDescription', models.CharField(db_index=True, default='empty', max_length=360, verbose_name='توضیحات کوتاه')),
                ('Description', models.TextField(db_index=True, verbose_name='توضیحات اصلی')),
                ('isActive', models.BooleanField(default=False, verbose_name='فعال /غیر فعال')),
                ('slug', models.SlugField(blank=True, default='', max_length=200, unique=True)),
                ('isDelete', models.BooleanField(verbose_name='حذف شده / نشده')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=300, verbose_name='عنوان')),
                ('urlTitle', models.CharField(db_index=True, max_length=300, verbose_name='Url عنوان در')),
                ('isActive', models.BooleanField(verbose_name='فعال / غیرفعال')),
            ],
            options={
                'verbose_name': 'دسته بندی محصول',
                'verbose_name_plural': 'دسته بندی  های محصولات',
            },
        ),
        migrations.CreateModel(
            name='ProductTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(db_index=True, max_length=300, verbose_name='تگ محصول')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_tags', to='productapp.product')),
            ],
            options={
                'verbose_name': 'تگ محصول',
                'verbose_name_plural': 'تگ های محصولات',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='productCategories', to='productapp.productcategory', verbose_name='دسته بندی محصول'),
        ),
    ]
