from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexPage, name='home-page'),
    path('contact-us', views.contactPage, name='contact-us-page'),
    # path('site-header', views.siteHeaderPartial, name='site-header-partial')
    # path('site-footer', views.siteFooterPartial, name='site-footer-partial')

]
