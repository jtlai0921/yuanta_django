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
]
