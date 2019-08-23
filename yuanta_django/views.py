import time

from captcha.helpers import captcha_image_url
from captcha.models import CaptchaStore
from django.contrib import auth
from django.http import HttpResponse, QueryDict
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from yuanta_django.utils import CaptchaCheck


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
    username = request.COOKIES['username'] if 'username' in request.COOKIES else ''
    password = request.COOKIES['password'] if 'password' in request.COOKIES else ''
    remember = request.COOKIES['remember'] if 'remember' in request.COOKIES else ''

    # 圖片驗證碼
    # hashkey 驗證碼生成的祕鑰
    hashkey = CaptchaStore.generate_key()
    # image_url驗證碼的圖片地址
    image_url = captcha_image_url(hashkey)

    response = render(request, 'user_login_form.html', locals())
    return response


def user_login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    # 取得驗證碼
    captchaCheck = CaptchaCheck(request.POST)

    # 驗證驗證碼
    if captchaCheck.is_valid():
        # 驗證使用者帳密
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # 進行登入, 存入 session 物件
            auth.login(request, user)
            response = HttpResponse("Login success: " + str(user))
            # 存入 Cookies
            remember = request.POST.get('remember', False)
            if remember:  # 存入 cookie
                response.set_cookie('username', username)
                response.set_cookie('password', password)
                response.set_cookie('remember', 'checked')
            else:  # 清除 cookie
                response.delete_cookie('username')
                response.delete_cookie('password')
                response.delete_cookie('remember')

            return response
        else:
            return HttpResponse("Login fail")

    else:
        return HttpResponse("驗證碼 error !")


def user_logout(request):
    auth.logout(request)
    return HttpResponse('User logout')


def user_crud_form(request):
    flag = request.user.is_authenticated
    if flag:
        return render(request, 'user_crud_form.html')
    else:
        return HttpResponse('尚未登入')
