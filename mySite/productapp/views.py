from django.shortcuts import render, get_object_or_404
from .models import product
from django.views.generic.base import TemplateView
from django.views.generic import ListView

class ProductDetailsView(ListView):
    template_name = 'productapp/productDetails.html'

    def get_queryset(self):
        pass

# class ProductDetailsView(TemplateView):
#     template_name = 'productapp/productDetails.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(ProductDetailsView, self).get_context_data()
#         slug = kwargs['slug']
#         productInstance = get_object_or_404(product, slug=slug)
#         context['product'] = productInstance
#         return context


# def showProductDetail(request, slug):
#     productC = get_object_or_404(product, slug=slug)
#     return render(request, 'productapp/productDetails.html', {'productC': productC})

# def showProductList(request):
#     productAll = product.objects.all().order_by('price')[:5]
#     return render(request, 'productapp/productsList.html', {'productAll': productAll})

# class ProductListView(TemplateView):
#     template_name = 'productapp/productsList.html'
#
#     def get_context_data(self, **kwargs):
#         products = product.objects.all().order_by('price')[:5]
#         context = super(ProductListView, self).get_context_data()
#         context['products'] = products
#         return context

class ProductListView(ListView):
    template_name = 'productapp/productsList.html'
    model = product
    context_object_name = 'products'

    def get_queryset(self):
        base_query = super(ProductListView, self).get_queryset()
        data = base_query.filter(isActive=True)
        return data
