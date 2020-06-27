from django.shortcuts import render, HttpResponse
from main_pro.models import user_information


# Create your views here.
def printer(request):
    return render(request, "login.html")


def login(request):
    data = request.GET
    user_name = data["entry_name"]
    user_pwd = data["entry_pwd"]
    print(user_name, user_pwd)
    try:
        user = user_information.objects.get(name=user_name)
        if user_pwd == user.password:
            return HttpResponse("welcome" + user_name)
        else:
            return HttpResponse("error,用户名或者密码错误")
    except:
        return HttpResponse("error,用户不存在")
