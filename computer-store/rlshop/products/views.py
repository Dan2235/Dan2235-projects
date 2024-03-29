from django.shortcuts import render, redirect
from .models import Product
from main.models import Account, User


def get_end(count):
    end = ""

    if count in range(1, 111, 10):
        if count in (11, 111):
            end = "s"
        else:
            end = ""
    else:
        end = "s"

    return end

def put_to_cart(request, product):
    try:
        email = request.COOKIES["email"]
        pr = request.COOKIES["products"] + product + "|"
        resp = redirect("/user-data")
        resp.set_cookie("products", pr)
        acc = Account.objects.get(email=email)
        acc.user.products = pr
        acc.user.save(update_fields=["products"])
        return resp
    except:
        return redirect("/")

def del_from_cart(request, product):
    email = request.COOKIES["email"]
    pr = request.COOKIES["products"]
    pr = pr.replace(f"{product}|", "")
    resp = redirect("/user-data")
    resp.set_cookie("products", pr)
    acc = Account.objects.get(email=email)
    acc.user.products = pr
    acc.user.save(update_fields=["products"])
    return resp

def videocards(request):
    pr = Product.objects.filter(type="Videocard")
    try:
        p = request.COOKIES["products"]
    except:
        p = ""
    count = len(pr)
    end = get_end(count)

    return render(request, "videocards.html", 
        {"pr": pr, "count": count, "end": end, "p": p}
    )

def processors(request):
    pr = Product.objects.filter(type="Processor")
    try:
        p = request.COOKIES["products"]
    except:
        p = ""
    count = len(pr)
    end = get_end(count)

    return render(request, "processors.html", 
        {"pr": pr, "count": count, "end": end, "p": p}
    )