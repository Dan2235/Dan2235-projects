from django.shortcuts import render, redirect
from .forms import *
from .models import *

forb = "Incorrect email or password. Try again."
forb2 = "User with this email already exist. Try again."

uform = UserForm()
aform = AccountForm()

def index(request):
    try:
        name = request.COOKIES["name"]
        #age = request.COOKIES["age"]
        #email = request.COOKIES["email"]
        #products = request.COOKIES["products"]
        udata ={"name": name}
        return render(request, "index.html", {"udata": udata})
    except:
        return render(request, "index.html", {"udata": ""})

def user_data(request):
    name = request.COOKIES["name"]
    age = request.COOKIES["age"]
    email = request.COOKIES["email"]
    products_ck = request.COOKIES["products"]
    products = []
    udata = {"name": name, "age": age, "email": email}
    j = ""

    for i in products_ck:
        if i == "|":
            products.append(j)
            j = ""
        else:
            j += i
    
    return render(request, "user-data.html", 
        {"udata": udata, "products": products}
    )

def sign_in(request):
    return render(request, "sign-in.html", 
        {"text": "Sign in", "form": uform}
    )

def try_sign_in(request):
    if request.method == "POST":
        usform = UserForm(request.POST)
        if usform.is_valid():
            accounts = Account.objects.all()
            email = usform.cleaned_data["email"]
            password = usform.cleaned_data["password"]
            data_checked = False

            for i in accounts:
                if i.email == email and\
                    i.password == password:
                        data_checked = True
                        resp = render(request, "sign-in-2.html")
                        resp.set_cookie("name", i.user.name)
                        resp.set_cookie("age", i.user.age)
                        resp.set_cookie("email", i.email)
                        resp.set_cookie("products", i.user.products)
                        return resp
                
            if data_checked == False:
                return render(request, "sign-in.html", 
                    {"text": forb, "form": uform},
                    status=403
                )

def sign_out(request):
    resp = redirect("/")
    resp.delete_cookie("name")
    resp.delete_cookie("age")
    resp.delete_cookie("email")
    resp.delete_cookie("products")
    return resp

def sign_up(request):
    return render(request, "sign-up.html", 
        {"text": "Sign up", "form": aform}
    )

def try_sign_up(request):
    if request.method == "POST":
        usform = AccountForm(request.POST)
        if usform.is_valid():
            accounts = Account.objects.all()
            email = usform.cleaned_data["email"]
            password = usform.cleaned_data["password"]
            name = usform.cleaned_data["name"]
            age = usform.cleaned_data["age"]
            user_exist = False

            for i in accounts:
                if i.email == email:
                    user_exist = True
                    break

            if user_exist == False:
                user = User.objects.create(name=name,age=age)
                Account.objects.create(email=email, password=password,
                    user=user
                )
                print("Registrated: ", email, password, name, age)                  
                return render(request, "sign-up-2.html")
            else:
                return render(request, "sign-up.html",
                    {"text": forb2, "form": aform}, status=403
                )

def pulse_animation(request):
    return render(request, "pulse-animation.html") 