from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *


def index(request):
    return render(request, 'HomePage/index.html')


# 用户注册
def register(request):
    if request.method == "GET": #登录页面请求方式为GET ，？
        context = {}
        context['previous_page'] = request.GET.get('from_page')
        return render(request, 'HomePage/register.html', context)
    else:
        try:
            username = request.POST['username']
            password = request.POST['password']
            # 检查是否存在相同用户名信息
            if User.objects.filter(username=username).exists():
                context = {}
                context['register_info'] = True
                context['previous_page']=request.GET.get('from_page') #record the page before register
                return render(request, 'HomePge/register.html', context)
            else:
                user = User.objects.create_user(username=username, password=password) #创建新用户
                user.save() #保存新用户信息
                return HttpResponseRedirect(request.GET.get('from_page')) #转回注册前界面
        except:
            return HttpResponse('Sorry,something goes wrong')

# 用户注销
def logout(request):
    auth.logout(request)
    #return HttpResponseRedirect(request.GET.get('from_page'))
    return render(request, 'HomePage/index.html')

#用户登录
def login(request):
    if request.method == "GET": #如果请求为GET，则是直接转到login界面
        context = {}
        context['previous_page'] = request.GET.get('from_page') #记录登录之前的界面
        return render(request, 'HomePage/login.html', context)
    else:
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = authenticate(request, username=username, password=password)
            auth.login(request, user)
            return HttpResponseRedirect(request.GET.get('from_page')) #转回登录之前的界面
        except:
            context = {}
            context['login_info'] = True
            context['previous_page']=request.GET.get('from_page')
            return render(request, 'HomePage/login.html', context)