from django.shortcuts import render


def indexPage(request):
    return render(request, 'homeapp/index_page.html')


def contactPage(request):
    return render(request, 'homeapp/contact_page.html')


def siteHeaderPartial(request):
    return render(request, '../templates/base/siteHeaderPartial.html', {})


def siteFooterPartial(request):
    return render(request, '../templates/base/siteFooterPartial.html', {})
