from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path


def hello(request):
    return HttpResponse("Hello Django")


def test(request):
    return render(request, 'test.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),

    path('test/', test)
]
