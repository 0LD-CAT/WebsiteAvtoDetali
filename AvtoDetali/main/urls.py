from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('catalog', views.catalog, name='catalog'),
    path('contacts', views.contacts, name='contacts'),
    path('delivery', views.delivery, name='delivery'),
    path('news', views.news, name='news')
]