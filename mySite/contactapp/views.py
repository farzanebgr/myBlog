from django.shortcuts import render, redirect
from django.views import View
from .forms import contactUsForm, contactUsModelForm
from .models import contactUs
from django.urls import reverse


class contactUsView(View):
    def get(self, request):
        contactForm = contactUsModelForm()
        return render(request, 'contactusapp/contact_us.html', {
            'contactForm': contactForm
        })

    def post(self, request):
        contactForm2 = contactUsModelForm(request.POST)
        if contactForm2.is_valid():
            contactForm2.save()
            return redirect('home-page')


def contactUsPage(request):
    if request.method == 'POST':
        contactForm2 = contactUsModelForm(request.POST)
        if contactForm2.is_valid():
            contactForm2.save()
            return redirect('home-page')
    contactForm = contactUsModelForm()
    return render(request, 'contactusapp/contact_us.html', {
        'contactForm': contactForm
    })
