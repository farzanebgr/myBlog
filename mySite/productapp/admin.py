from django.contrib import admin
from . import models


class ProductAdmin(admin.ModelAdmin):
    list_filter = ['title', 'isActive']
    list_display = ['title', 'price', 'isActive', 'isDelete']
    list_editable = ['price', 'isActive']


admin.site.register(models.product, ProductAdmin)
admin.site.register(models.ProductCategory)
admin.site.register(models.ProductTags)
admin.site.register(models.ProductBrand)

