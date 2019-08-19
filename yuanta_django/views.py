import time

from django.http import HttpResponse, QueryDict
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


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
    dict['amount'] = len(users)
    return render(request, 'hello_users.html', dict)


def hello_template_users2(request):
    users = [
        {'name': 'vincent', 'age': 30},
        {'name': 'anita', 'age': 28},
        {'name': 'howard', 'age': 15},
        {'name': 'joanna', 'age': 10}
    ]
    amount = len(users)
    title = '我的成員'
    nodata = '沒有資料'
    copyright = '版權所有 @2019'

    return render(request, 'hello_users2.html', locals())


def http_method_form(request):
    return render(request, 'http_method_form.html')


#@csrf_exempt  # csrf 豁免
def http_method_result(request):
    # 取得 headers
    for key in request.META:
        print(key, '=', request.META.get(key, ''))
    text = ''
    if request.method == 'GET':
        text = request.GET.get('text', '')


    # time.sleep(5)
    return HttpResponse('http_method_result, method:' + request.method + ', text:' + text)

