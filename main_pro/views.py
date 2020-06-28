from django.shortcuts import render, HttpResponse
from main_pro.models import user_information


# Create your views here.
def printer(request):
    data=user_information.objects.all()
    print(data)
    return render(request, "login.html")


def login(request):
    data = request.GET
    user_name = data["entry_name"]
    user_pwd = data["entry_pwd"]
    print(data)
    try:
        user = user_information.objects.get(name=user_name)
        print(user.password)
        if user_pwd == user.password:
            return HttpResponse("welcome" + user_name)
        else:
            return HttpResponse("error,用户名或者密码错误")
    except:
        return HttpResponse("error,用户不存在")

#注册用户
def resgister(request):
    data = request.GET
    user_name = data["entry_name"]
    user_pwd = data["entry_pwd"]
    print(data)
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

