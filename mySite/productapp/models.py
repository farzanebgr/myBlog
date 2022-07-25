from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify


class ProductCategory(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان')
    urlTitle = models.CharField(max_length=300, db_index=True, verbose_name='Url عنوان در')
    isActive = models.BooleanField(verbose_name='فعال / غیرفعال')

    def __str__(self):
        return f'{self.title} - {self.urlTitle}'

    class Meta:
        verbose_name = 'دسته بندی محصول'
        verbose_name_plural = 'دسته بندی  های محصولات'


class product(models.Model):
    title = models.CharField(max_length=300, verbose_name='نام')
    category = models.ManyToManyField(ProductCategory, related_name='productCategories', verbose_name='دسته بندی محصول')
    price = models.IntegerField(verbose_name='قیمت')
    shortDescription = models.CharField(max_length=360, db_index=True, default='empty', verbose_name='توضیحات کوتاه')
    Description = models.TextField(db_index=True, verbose_name='توضیحات اصلی')
    isActive = models.BooleanField(default=False, verbose_name='فعال /غیر فعال')
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=200, unique=True)
    isDelete = models.BooleanField(verbose_name='حذف شده / نشده')

    def get_absolute_url(self):
        return reverse('product-details-page', args=[self.slug])

    def save(self, *args, **keyargs):
        self.slug = slugify(self.title)
        super().save(*args, **keyargs)

    def __str__(self):
        return f"{self.title} ({self.price})"

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ProductTags(models.Model):
    caption = models.CharField(max_length=300, db_index=True, verbose_name='تگ محصول')
    product = models.ForeignKey(product, on_delete=models.CASCADE, related_name='product_tags')

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural = 'تگ های محصولات'
