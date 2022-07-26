from django.shortcuts import render, redirect
from django.urls import reverse


def contactUsPage(request):
    if request.method == 'POST':
        print(request.POST['name'])
        print(request.POST['email'])
        print(request.POST['subject'])
        print(request.POST['message'])
        return redirect(reverse('home-page'))

    return render(request, 'contactusapp/contact_us.html', {})
