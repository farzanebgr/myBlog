from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>', views.ProductDetailsView.as_view(), name='product-details-page'),
    path('productslist/', views.ProductsView.as_view(), name='product-list-page'),
    path('list/', views.ProductListView.as_view(), name='products-page'),
]
