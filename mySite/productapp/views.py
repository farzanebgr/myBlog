from django.shortcuts import render


def showIndexPage(request):
    return render(request, 'productapp/index.html')


