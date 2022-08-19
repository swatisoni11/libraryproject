"""libraryproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the included() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from libraryapp.views import index
#from . import views

urlpatterns = [

    #path("", views.index, name="index"),

    #path('index/',index , name="index"),
    #path('booklist', BooklistView.as_view(), name="book-list"),
    #path('bookcreate', BookCreateView.as_view(), name="book-create"),
    #path('bookdetail', BookDetailView.as_view(), name="book-detail"),
]