from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class registerForm(forms.Form):
    username = forms.CharField(
        label='نام کاربری',
        widget=forms.TextInput(),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    first_name = forms.CharField(
        label='نام',
        widget=forms.TextInput(),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    last_name = forms.CharField(
        label='نام خانوادگی',
        widget=forms.TextInput(),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    age = forms.IntegerField(
        label='سن',
        widget=forms.NumberInput(),
    )
    gender = forms.BooleanField(
        label='جنسیت',
        widget=forms.CheckboxInput(),
    )
    phone = forms.CharField(
        label='تلفن',
        widget=forms.TextInput(),
        validators=[
            validators.MaxLengthValidator(11),
        ]
    )
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator,
        ]
    )
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    confirm_password = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password

        raise ValidationError('کلمه عبور و تکرار کلمه عبور مغایرت دارند')


class loginForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )
