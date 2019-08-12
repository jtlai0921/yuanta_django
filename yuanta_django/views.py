from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello Django")

def test(request):
    return render(request, 'test.html')

def hello_name(request, name):
    return HttpResponse("Hello " + name)

def hello_add(request, x, y):
    sum = int(x) + int(y)
    return HttpResponse("%d + %d = %d" % (x, y, sum))
