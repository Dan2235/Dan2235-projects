from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from .forms import *
from .models import *

forb = "Incorrect username or password. Try again."
forb2 = "User with this username already exist. Try again."
uform = SignInForm()
aform = SignUpForm()

def index(request):
    try:
        user_name = request.COOKIES["user_name"]
        return render(request, "index.html", {"udata": user_name})            
    except:
        return render(request, "index.html", {"udata": ""})

def my_channel(request):
    user_name = request.COOKIES["user_name"]
    channel_name = request.COOKIES["channel_name"]
    subscribers = request.COOKIES["subscribers"]
    udata = {"user_name": user_name, "channel_name": channel_name,
        "subscribers": subscribers 
    }
    return render(request, "my-channel.html", {"udata": udata})

def user(request, user_name):
    user = User.objects.get(user_name=user_name)
    if user.user_name == request.COOKIES["user_name"]:
        return redirect("/mychannel")
    else:
        posts = Post.objects.get(user=user)
        return render(request, "user.html", {"user": user, "posts": posts})

def edit(request, type):
    if type == "channel_name":
        name = request.COOKIES["channel_name"]
    else:
        name = request.COOKIES["user_name"]
    
    return render(request, "edit.html", {"name": name, "type": type})

def try_edit(request, type):
    if request.method == "POST":
        user_name = request.COOKIES["user_name"]
        new_name = request.POST.get["new_name"]
        user = User.objects.get(user_name=user_name)
        if type == "channel_name":
            user.channel_name = new_name
        else:
            un_busy = False
            for i in User.objects.all():
                if i.user_name == new_name:
                    un_busy = True
                    return HttpResponseForbidden("<h1>This username is busy")
            if not un_busy:
                user.user_name = new_name
        user.save()
        return redirect("/mychannel")

def sign_in(request):
    return render(request, "sign-in.html", 
        {"text": "Sign in", "form": uform}
    )

def try_sign_in(request):
    if request.method == "POST":
        usform = SignInForm(request.POST)
        if usform.is_valid():
            users = User.objects.all()
            user_name = usform.cleaned_data["user_name"]
            password = usform.cleaned_data["password"]
            data_checked = False

            for i in users:
                if i.user_name == user_name and\
                    i.password == password:
                        data_checked = True
                        resp = render(request, "sign-in-2.html")
                        resp.set_cookie("user_name", i.user_name)
                        resp.set_cookie("channel_name", i.channel_name)
                        resp.set_cookie("subscribers", i.subscribers)
                        return resp
                
            if data_checked == False:
                return render(request, "sign-in.html", 
                    {"text": forb, "form": uform},
                    status=403
                )

def sign_out(request):
    resp = redirect("/")
    resp.delete_cookie("user_name")
    resp.delete_cookie("channel_name")
    resp.delete_cookie("subscribers")
    return resp

def sign_up(request):
    return render(request, "sign-up.html", 
        {"text": "Sign up", "form": aform}
    )

def try_sign_up(request):
    if request.method == "POST":
        usform = SignUpForm(request.POST)
        if usform.is_valid():
            users = User.objects.all()
            user_name = usform.cleaned_data["user_name"]
            password = usform.cleaned_data["password"]
            channel_name = usform.cleaned_data["channel_name"]
            user_exist = False

            for i in users:
                if i.user_name == user_name:
                    user_exist = True
                    break

            if user_exist == False:
                User.objects.create(user_name=user_name,
                    channel_name=channel_name, password=password,
                    subscribers=0
                )
                print("Registrated: ", user_name, password)                  
                return render(request, "sign-up-2.html")
            else:
                return render(request, "sign-up.html",
                    {"text": forb2, "form": aform}, status=403
                )