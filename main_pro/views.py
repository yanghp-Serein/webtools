from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from main_pro.models import user_information
import json


# Create your views here.
def printer(request):
    # u = user_information.objects.all()
    # print(u)
    data=user_information.objects.all()
    print(data)
    return render(request, "login.html")


def login(request):
    data = request.POST
    user_name = data["entry_name"]
    user_pwd = data["entry_pwd"]
    result = {}
    print(data)
    try:
        user = user_information.objects.get(name=user_name)
        print(user.password)
        if user_pwd == user.password:
            result["status"] = 1
            result["title"] = "success"
        else:
            result["status"] = 0
            result["title"] = "error"
    except:
        result["status"] = 2
        result["title"] = "error"
    print(result)
    results = json.dumps(result)
    print("result", results, type(results))
    return HttpResponse(results)


# 点击确定实现数据提交 将用户和密码存入数据库中
    return HttpResponse("error,用户不存在")

#注册用户
def resgister(request):
    data = request.GET
    user_name = data["entry_name"]
    user_pwd = data["entry_pwd"]
    print(data)
    try:
        user = user_information.objects.get(name=user_name)
        if user_name == user.name:
            return HttpResponse("该用户名已经存在!")
    except:
        user = user_information.objects.create(name=user_name, password=user_pwd)
        user.save()
        return HttpResponse("注册成功！")


def person(request):
    data = request.GET
    user_name = data["entry_name"]
    return render(request, "person.html",user_name)
    # u = user_information.objects.all()
    #     # print("f", u)
    try:
        user = user_information.objects.get(name=user_name)
        if user_name == user.name:
            return HttpResponse("该用户名已存在！")
    except:
        user_information(name=user_name,password=user_pwd)
        return HttpResponse("注册成功！！")

def person(request):
    # data = request.GET
    # user_name = data["entry_name"]
    return render(request,"person.html")

