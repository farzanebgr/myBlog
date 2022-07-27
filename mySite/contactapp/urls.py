from django.urls import path
from . import views

urlpatterns = [
    # path('', views.contactUsPage, name='contact-us-page')
    path('', views.contactUsView.as_view(), name='contact-us-page')
]
