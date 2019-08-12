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

def add_get(request):
    x = int(request.GET['x'])
    y = int(request.GET['y'])
    sum = x + y
    return HttpResponse("%d + %d = %d" % (x, y, sum))

def hello_template_name(request, name):
    dict = {'name': name}
    return render(request, 'hello_name.html', dict)

def hello_template_users(request):
    dict = {}
    users = [
        {'name': 'vincent', 'age': 30},
        {'name': 'anita', 'age': 28},
        {'name': 'howard', 'age': 15},
        {'name': 'joanna', 'age': 10}
    ]
    dict['users'] = users
    return render(request, 'hello_users.html', dict)
