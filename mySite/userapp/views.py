from django.shortcuts import render


def showRegistrationPage(request):
    return render(request, 'userapp/registration.html')


def showLoginPage(request):
    return render(request, 'userapp/login.html')
