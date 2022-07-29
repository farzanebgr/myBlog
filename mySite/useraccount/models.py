from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    age = models.IntegerField(verbose_name='سن', null=True, blank=True)
    gender = models.BooleanField(verbose_name='جنسیت', choices=[(0, 'مرد'), (1, 'زن')], null=True, blank=True)
    phone = models.CharField(max_length=11, verbose_name='تلفن همراه', null=True, blank=True)

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.get_full_name()
