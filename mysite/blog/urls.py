from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home/', views.homepage, name = "homepage"),
    path('about/', views.about, name = "about"),
    path('contacts/', views.contacts, name = "contacts"),
    path('news/', views.news, name = "news"),
]