from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View


# def indexPage(request):
#     return render(request, 'homeapp/index_page.html')

# class homeView(View):
#     def get(self, request):
#         context = {
#             'data': 'this is a data...'
#         }
#         return render(request, 'homeapp/index_page.html', context)
class homeView(TemplateView):
    template_name = 'homeapp/index_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = 'THIS IS DATA'
        return context


def siteHeaderPartial(request):
    return render(request, '../templates/base/siteHeaderPartial.html', {})


def siteFooterPartial(request):
    return render(request, '../templates/base/siteFooterPartial.html', {})
