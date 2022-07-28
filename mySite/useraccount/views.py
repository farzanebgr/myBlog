from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from useraccount.forms import registerForm
from .models import User
from django.utils.crypto import get_random_string


class registerView(View):
    def get(self, request):
        register_form = registerForm()
        context = {
            'register_form': register_form
        }
        return render(request, 'useraccount/registerForm.html', context)

    def post(self, request):
        register_form = registerForm(request.POST)
        if register_form.is_valid():
            userEmail = register_form.cleaned_data.get('email')
            userPassword = register_form.cleaned_data.get('password')
            user = User.objects.filter(email__iexact=userEmail).exists()
            if user:
                register_form.add_error('email', 'ایمیل وارد شده تکراری می باشد.')
            else:
                newUser = User(email=userEmail,
                               emailActiveCode=get_random_string(72),
                               is_active=False)
                newUser.set_password(userPassword)
                newUser.save()
                # todo: send email active code
                return redirect(reverse('login-page'))

        context = {
            'register_form': register_form
        }
        return render(request, 'useraccount/registerForm.html', context)


class loginView(View):
    def get(self, request):
        context = {
            'login_form': None
        }
        return render(request, 'useraccount/registerForm.html', context)

    def post(self, request):
       pass

