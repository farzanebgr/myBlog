from django.shortcuts import render, get_object_or_404
from .models import product
from django.db.models import Avg


def showProductList(request):
    productAll = product.objects.all().order_by('price')[:5]
    return render(request, 'productapp/productsList.html', {'productAll': productAll})


def showProductDetail(request, slug):
    productC = get_object_or_404(product, slug=slug)
    return render(request, 'productapp/productDetails.html', {'productC': productC})
