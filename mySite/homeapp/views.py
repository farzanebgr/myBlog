from django.shortcuts import render
from django.views.generic.base import TemplateView

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
