from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .models import User
from django.utils.crypto import get_random_string
from django.http import Http404, HttpRequest
from django.contrib.auth import login, logout

from useraccount.forms import registerForm, loginForm


class RegisterView(View):
    def get(self, request):
        register_form = registerForm()
        context = {
            'register_form': register_form
        }
        return render(request, 'useraccount/registerForm.html', context)

    def post(self, request):
        register_form = registerForm(request.POST)
        if register_form.is_valid():
            user_username = register_form.cleaned_data.get('username')
            user_first_name = register_form.cleaned_data.get('first_name')
            user_last_name = register_form.cleaned_data.get('last_name')
            user_age = register_form.cleaned_data.get('age')
            user_gender = register_form.cleaned_data.get('gender')
            user_phone = register_form.cleaned_data.get('phone')
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'ایمیل وارد شده تکراری می باشد')
            else:
                new_user = User(
                    age=user_age,
                    username=user_username,
                    last_name=user_last_name,
                    first_name=user_first_name,
                    gender=user_gender,
                    phone=user_phone,
                    email=user_email,
                    email_active_code=get_random_string(72),
                    is_active=False)
                new_user.set_password(user_password)
                new_user.save()
                return redirect(reverse('login-page'))
        context = {
            'register_form': register_form
        }

        return render(request, 'useraccount/registerForm.html', context)


class LoginView(View):
    def get(self, request):
        login_form = loginForm()
        context = {
            'login_form': login_form
        }

        return render(request, 'useraccount/loginForm.html', context)

    def post(self, request: HttpRequest):
        login_form = loginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_pass = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'حساب کاربری شما فعال نشده است')
                else:
                    is_password_correct = user.check_password(user_pass)
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse('home_page'))
                    else:
                        login_form.add_error('email', 'کلمه عبور اشتباه است')
            else:
                login_form.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')

        context = {
            'login_form': login_form
        }

        return render(request, 'useraccount/loginForm.html', context)
