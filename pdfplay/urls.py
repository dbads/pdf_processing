from django.contrib import admin
from django.urls import path

from .views import pdf_play

urlpatterns = [
    path('', pdf_play, name='pdf_play'),
]