from django.shortcuts import render
from django.urls import path

from productExplorer import views

app_name = "productExplorer"

urlpatterns = [
    path('', views.index, name='index'),
    path('viewProduct/', views.viewProduct, name='viewProduct'),
    path('viewProduct/<uuid:id>', views.viewProduct, name='viewProduct')
]


