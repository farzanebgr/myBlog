from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateView

from productapp.models import product
from siteapp.models import siteSetting, footerLinkBox


class homeListView(ListView):
    template_name = 'homeapp/index_page.html'
    model = product
    context_object_name = 'products'
    ordering = ['price']

    def get_context_data(self, **kwargs):
        base_query = super(homeListView, self).get_queryset()
        data1 = base_query.filter(category=1)
        data2 = base_query.filter(category=2)
        data3 = base_query.filter(category=3)
        setting: siteSetting = siteSetting.objects.filter(isMainSettings=True).first()
        context = {
            'site_Settings': setting,
            'data1': data1,
            'data2': data2,
            'data3': data3,
        }
        return context


class aboutView(TemplateView):
    template_name = 'homeapp/about_page.html'

    def get_context_data(self, **kwargs):
        context = super(aboutView, self).get_context_data(**kwargs)
        site_Setting = siteSetting.objects.filter(isMainSettings=True).first()
        context['site_Setting'] = site_Setting
        return context


def siteHeaderPartial(request):
    setting: siteSetting = siteSetting.objects.filter(isMainSettings=True).first()
    context = {
        'site_Settings': setting
    }
    return render(request, 'base/siteHeaderPartial.html', context)


def siteFooterPartial(request):
    setting: siteSetting = siteSetting.objects.filter(isMainSettings=True).first()
    footer_link_boxes = footerLinkBox.objects.all()
    for item in footer_link_boxes:
        item.footerlink_set

    context = {
        'site_Settings': setting,
        'footer_link_boxes': footer_link_boxes
    }
    return render(request, 'base/siteFooterPartial.html', context)
