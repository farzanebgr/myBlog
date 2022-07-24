from django.urls import path
from . import views

urlpatterns = [
    path('', views.showIndexPage, name='index-page')
]
