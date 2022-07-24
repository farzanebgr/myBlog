from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.showRegistrationPage, name='registration-page'),
    path('login/', views.showLoginPage, name='login-page')

]

