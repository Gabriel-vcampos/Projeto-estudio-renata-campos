from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('home.urls')),
    path('home/', include('home.urls')),
]
