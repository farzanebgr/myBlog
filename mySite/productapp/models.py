from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify


class ProductCategory(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان دسته بندی')
    urlTitle = models.CharField(max_length=300, db_index=True, verbose_name='Url عنوان در')
    image = models.ImageField(upload_to='images/category', null=True, blank=True, verbose_name='تصویر دسته بندی')
    isActive = models.BooleanField(verbose_name='فعال / غیرفعال')
    isDelete = models.BooleanField(verbose_name='حذف شده / نشده', null=True)

    def __str__(self):
        return f'{self.title} - {self.urlTitle}'

    class Meta:
        verbose_name = 'دسته بندی محصول'
        verbose_name_plural = 'دسته بندی  های محصولات'


class ProductBrand(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='نام برند')
    isActive = models.BooleanField(verbose_name='فعال / غیرفعال')

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'

    def __str__(self):
        return self.title


class product(models.Model):
    title = models.CharField(max_length=300, verbose_name='نام محصول')
    category = models.ManyToManyField(ProductCategory, related_name='productCategories', verbose_name='دسته بندی محصول')
    image = models.ImageField(upload_to='images/products', null=True, blank=True, verbose_name='تصویر محصول')
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, verbose_name='برند', null=True, blank=True)
    price = models.IntegerField(verbose_name='قیمت')
    numbers = models.IntegerField(verbose_name='تعداد', null=True, blank=True)
    dateOfCreate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ثبت')
    shortDescription = models.CharField(max_length=360, db_index=True, default='empty', verbose_name='توضیحات کوتاه')
    Description = models.TextField(db_index=True, verbose_name='توضیحات اصلی')
    isActive = models.BooleanField(default=False, verbose_name='فعال /غیر فعال')
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=200, unique=True,
                            verbose_name='عنوان در url')
    isDelete = models.BooleanField(verbose_name='حذف شده / نشده')

    def get_absolute_url(self):
        return reverse('product-details-page', args=[self.slug])

    def save(self, *args, **keyargs):
        super().save(*args, **keyargs)

    def __str__(self):
        return f"{self.title} ({self.price})"

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


class ProductTags(models.Model):
    caption = models.CharField(max_length=300, db_index=True, verbose_name='تگ محصول')
    product = models.ForeignKey(product, on_delete=models.CASCADE, related_name='product_tags')

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural = 'تگ های محصولات'
