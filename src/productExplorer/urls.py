from django.shortcuts import render
from django.urls import path


def default(request):
    return render(request, 'index.html', context=None)


urlpatterns = [
    path('', default),
]


