from django.http import request
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import product, ProductBrand, ProductCategory
from django.views.generic.base import TemplateView, View
from django.views.generic import ListView, DetailView


class ProductDetailsView(DetailView):
    template_name = 'productapp/productDetails.html'
    model = product


class ProductListView(ListView):
    template_name = 'productapp/productsList.html'
    model = product
    context_object_name = 'products'
    ordering = ['price']
    paginate_by = 6

    def get_queryset(self):
        base_query = super(ProductListView, self).get_queryset()
        data = base_query.filter(isActive=True)
        return data


class CategoryListView(ListView):
    template_name = 'productapp/incloudes/brandItems.html'
    model = ProductBrand
    context_object_name = 'category'

    def CategoryList(request):
        Category_List = ProductCategory.objects.all()
        for item in Category_List:
            item.Category_List_set

        context = {
            'Category_List': Category_List
        }
        return render(request, 'productapp/incloudes/brandItems.html', context)


class AddProductFavorite(View):
    def post(self, request):
        product_id = request.POST["product_id"]
        product1 = product.objects.get(pk=product_id)
        request.session["product_favorite"] = product_id
        return redirect(product1.get_absolute_url())


class ProductsView(ListView):
    template_name = 'productapp/productPage.html'
    model = product
    context_object_name = 'products'
    ordering = ['price']
    paginate_by = 2

    def get_queryset(self):
        base_query = super(ProductsView, self).get_queryset()
        data = base_query.filter(isActive=True)
        return data
