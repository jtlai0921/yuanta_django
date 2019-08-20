from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
import yuanta_django.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('test/', views.test),
    path('hello/<str:name>', views.hello_name),
    path('hello/add/<int:x>/<int:y>', views.hello_add),
    # /hello/add_get/?x=100&y=200
    path('hello/add_get/', views.add_get),

    path('hello_template/<str:name>', views.hello_template_name),
    path('hello_template_users/', views.hello_template_users),
    path('hello_template_users2/', views.hello_template_users2),

    path('http_method_form/', views.http_method_form),
    path('http_method_result/', views.http_method_result),

    path('hello_poll_form/', views.hello_poll_form),
    path('hello_poll_result/', views.hello_poll_result),

    path('hello_rating/', views.hello_rating),
    path('hello_rating_result/', views.hello_rating_result),
]
