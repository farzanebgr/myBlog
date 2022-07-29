from django.db import models


class siteSetting(models.Model):
    siteName = models.CharField(max_length=200, verbose_name='نام سایت')
    siteUrl = models.CharField(max_length=200, verbose_name='دامنه سایت')
    address = models.CharField(max_length=200, verbose_name='آدرس سایت')
    phone = models.CharField(max_length=200, null=True, blank=True, verbose_name='تلفن سایت')
    fax = models.CharField(max_length=200, null=True, blank=True, verbose_name='فکس سایت')
    email = models.CharField(max_length=200, null=True, blank=True, verbose_name='ایمیل سایت')
    copyRight = models.CharField(max_length=200, verbose_name='متن کپی رایت سایت')
    siteLogo = models.ImageField(upload_to='images/siteSetting', verbose_name='لوگو سایت')
    aboutUs = models.TextField(verbose_name='درباره ما')
    isMainSettings = models.BooleanField(verbose_name='تنظیمات اصلی')

    def __str__(self):
        self.siteName

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنطیمات'


class footerLinkBox(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')

    class Meta:
        verbose_name = 'دسته بندی آدرس ها در فوتر'
        verbose_name_plural = 'دسته بندی های آدرس ها در فوتر'

    def __str__(self):
        return self.title


class footerLink(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url = models.URLField(max_length=500, verbose_name='لینک')
    footerLinkRelation = models.ForeignKey(to=footerLinkBox, on_delete=models.CASCADE, verbose_name='دسته بندی')

    class Meta:
        verbose_name = 'آدرس در فوتر'
        verbose_name_plural = 'آدرس ها در فوتر'

    def __str__(self):
        return self.title
