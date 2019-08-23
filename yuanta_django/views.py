import time

from captcha.helpers import captcha_image_url
from captcha.models import CaptchaStore
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
    #for key in request.META:
    #    print(key, '=', request.META.get(key, ''))
    # 觀察 body
    print(request.body)
    text = ''
    if request.method == 'GET':
        text = request.GET.get('text', '')
    elif request.method == 'POST':
        text = request.POST.get('text', '')
    elif request.method == 'PUT':
        body = QueryDict(request.body)
        text = body.get('text')
    elif request.method == 'DELETE':
        body = QueryDict(request.body)
        text = body.get('text')
    # time.sleep(5)
    return HttpResponse('http_method_result, method:' + request.method + ', text:' + text)


def hello_poll_form(request):
    response = render(request, 'hello_poll.html')
    return response


def hello_poll_result(request):
    body = QueryDict(request.body)
    votes = body.getlist('vote')
    list = []
    list.append({'name': '蔡先生', 'vote': votes[0]})
    list.append({'name': '韓小姐', 'vote': votes[1]})
    list.append({'name': '郭小姐', 'vote': votes[2]})
    list.append({'name': '林先生', 'vote': votes[3]})
    response = render(request, 'hello_poll_result.html', locals())
    return response


def hello_rating(request):
    return render(request, 'hello_rating.html')


def hello_rating_result(request):
    return HttpResponse('ok')


def user_login_form(request):
    # 取得 Cookies
    # 略 ...

    # 圖片驗證碼
    # hashkey 驗證碼生成的祕鑰
    hashkey = CaptchaStore.generate_key()
    # image_url驗證碼的圖片地址
    image_url = captcha_image_url(hashkey)

    response = render(request, 'user_login_form.html', locals())
    return response
