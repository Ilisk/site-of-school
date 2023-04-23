from django.contrib import admin
from django.urls import path, include
from django.conf import settings #add this
from django.conf.urls.static import static #add this
from mainpage import views
urlpatterns = [
    path('', views.mainpage),
]