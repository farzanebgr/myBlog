from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeListView.as_view(), name='home-page'),
    path('about-us/', views.aboutView.as_view(), name='about-us-page')

]
