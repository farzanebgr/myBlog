from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class registerForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput()
    )
    confrimPassword = forms.CharField(
        label='تکرار رمز عبور',
        widget=forms.PasswordInput()
    )

    def clean_confrimPassword(self):
        password = self.cleaned_data.get('password')
        confrimPassword = self.cleaned_data.get('confrimPassword')

        if password == confrimPassword:
            return confrimPassword

        raise ValidationError('رمز عبور و تکرار آن مغایرت دارد.')
