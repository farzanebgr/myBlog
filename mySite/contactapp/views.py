from django.views.generic import ListView

from .forms import contactUsModelForm
from django.views.generic.edit import CreateView
from .models import userProfile


class contactUsView(CreateView):
    form_class = contactUsModelForm
    template_name = 'contactusapp/contact_us.html'
    success_url = '/contact-us/'


class CreateProfileView(CreateView):
    template_name = 'contactusapp/createProfilePage.html'
    models = userProfile
    fields = '__all__'
    success_url = '/contact-us/create-profile'


class ProfileView(ListView):
    model = userProfile
    template_name = 'contactusapp/profileListPage.html'
    context_object_name = 'profiles'
