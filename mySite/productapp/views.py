from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import product
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


class AddProductFavorite(View):
    def post(self, request):
        product_id = request.POST["product_id"]
        product1 = product.objects.get(pk=product_id)
        request.session["product_favorite"] = product_id
        return redirect(product1.get_absolute_url())
