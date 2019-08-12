from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path


def hello(request):
    return HttpResponse("Hello Django")


def test(request):
    return render(request, 'test.html')

def hello_name(request, name):
    return HttpResponse("Hello " + name)

def hello_add(request, x, y):
    sum = int(x) + int(y)
    return HttpResponse("%d + %d = %d" % (x, y, sum))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('test/', test),
    path('hello/<str:name>', hello_name),
    path('hello/add/<int:x>/<int:y>', hello_add),
]
