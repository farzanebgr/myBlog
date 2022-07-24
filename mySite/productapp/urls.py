from django.urls import path
from . import views

urlpatterns = [
    path('', views.showProductList, name='product-list-page'),
    path('<slug:slug>', views.showProductDetail, name='product-details-page')
]
