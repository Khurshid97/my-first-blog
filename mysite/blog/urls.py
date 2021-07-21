from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('', views.homepage, name = "homepage"),
    path('view/<str:pk>/', views.viewphoto, name = "view"),
    path('about/', views.about, name = "about"),
    path('contacts/', views.contacts, name = "contacts"),
    path('news/', views.news, name = "news"),
]