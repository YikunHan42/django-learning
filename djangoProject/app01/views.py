from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    # due to app register order, not root, due to settings templates dirs
    return HttpResponse("Hello World")

def user_list(request):
    return render(request, "user_list.html")

def user_add(request):
    return HttpResponse("Add User")

def tpl(request):
    name = "Aiden"
    roles = {"Admin", "CEO"}
    user_info = {"name": "kenny", "salary": 100000, "role": "CEO"}

    data_list = [
        {"name": "kenny3", "salary": 100000, "role": "CEO"},
        {"name": "kenny1", "salary": 100000, "role": "CEO"},
        {"name": "kenny2", "salary": 100000, "role": "CEO"},
    ]
    return render(request, "tpl.html", {"n1": name, "n2": roles, 'n3': user_info, 'n4': data_list})

def news(req):
    import requests
    # res = requests.get("url")
    # data_list = res.json()
    # print(data_list)

    return render(req, "news.html")

def something(request):
    print(request.method)
    # transparent, URL
    print(request.GET)
    # implicit, request
    print(request.POST)

    #return render(request, "something.html", {"title": "coming"})

    return redirect("https://www.baidu.com")

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    print(request.POST)
    username = request.POST.get("user")
    password = request.POST.get("pwd")

    if username == 'root' and password == '123':
        # return HttpResponse("success")
        return redirect("https://www.baidu.com")
        #return HttpResponse("failure")
    return render(request, "login.html", {"error_msg": "wrong id or password"})

from app01.models import Department, UserInfo

def orm(request):
    Department.objects.create(title="IT")
    UserInfo.objects.create(name = "ykhan", password = "666")
    UserInfo.objects.create(name="Aiden", password="777")

    # UserInfo.objects.filter(id=3).delete()
    # Department.objects.all().delete()

    # queryset, similar to list
    # data_list = UserInfo.objects.all()
    # data_list= UserInfo.objects.filter(id=1)
    #
    # row_obj = UserInfo.objects.filter(id=1).first()
    # no for is required
    # print(row_obj.id, row_obj.name, row_obj.password, row_obj.age)
    # return HttpResponse("Success")
    # for obj in data_list:
    #     print(obj.id, obj.name, obj.password, obj.age)
    #
    # Userinfo.objects.all().update(password=999)
    # Userinfo.objects.filter(id=2).update(password=999)
    return HttpResponse("Success")

def info_list(request):
    data_list = UserInfo.objects.all()
    return render(request, "info_list.html", {"data_list": data_list})

def info_add(request):
    if request.method == "GET":
        return render(request, 'info_add.html')

    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    age = request.POST.get("age")

    UserInfo.objects.create(name = user, password = pwd, age = age)

    # return HttpResponse("Success")
    return redirect("/info/list/")

def info_delete(request):
    # get
    nid = request.GET.get('nid')
    UserInfo.objects.filter(id=nid).delete()
    # return HttpResponse("Success")
    return redirect("/info/list/")