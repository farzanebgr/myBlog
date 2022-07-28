from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product-list-page'),
    path('<slug:slug>', views.ProductDetailsView.as_view(), name='product-details-page'),
    path('product-favorite/', views.AddProductFavorite.as_view(), name='product-favorite-page'),
]
