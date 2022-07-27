from django import forms
from .models import contactUs


class contactUsForm(forms.Form):
    fullName = forms.CharField(label='نام',
                               max_length=50,
                               required=True,
                               error_messages={
                                   'required': ' برای ثبت پیام لازم است نام خود را درج کنید'
                               },
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'نام و نام خانوادگی خود'
                               }
                               ))
    title = forms.CharField(label='موضوع',
                            widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'موضوع پیام شما'
                            }
                            ))
    email = forms.EmailField(label='ایمیل',
                             required=True,
                             widget=forms.EmailInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'آدرس ایمیل'
                             }))
    message = forms.CharField(label='پیام',
                              required=True,
                              widget=forms.Textarea(
                                  attrs={
                                      'class': 'form-control',
                                      'placeholder': 'متن پیام شما',
                                      'id': 'message'
                                  }))


class contactUsModelForm(forms.ModelForm):
    class Meta:
        model = contactUs
        fields = ['title', 'email', 'fullName', 'message']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'fullName': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'message'
            })
        }
        labels = {
            'title': 'موضوع پیام شما',
            'email': 'آدرس ایمیل شما',
            'fullName': 'نام و نام خانوادگی شما',
            'message': 'متن پیام شما'
        }
        error_messages = {
            'fullName': {
                'required': 'نام و نام خانوادگی شما نیاز است. لطفا نام و نام خانوادگی خود را وارد کنید'
            }
        }

