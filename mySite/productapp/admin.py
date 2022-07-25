from django.contrib import admin
from . import models


admin.site.register(models.product)
admin.site.register(models.ProductCategory)
admin.site.register(models.ProductTags)

