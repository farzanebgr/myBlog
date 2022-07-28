from django.urls import path
from . import views

urlpatterns = [
    path('', views.contactUsView.as_view(), name='contact-us-page'),
    path('create-profile/', views.CreateProfileView.as_view(), name='create-profile-page'),
    path('profiles/', views.ProfileView.as_view(), name='profiles-page'),
]
