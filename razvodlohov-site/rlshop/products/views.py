from django.shortcuts import render, redirect
from .models import Product
from main.models import Account, User

nums = (2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54, 62, 63, 64)

def get_end(count):
    end = ""

    if count in range(1, 111, 10):
        if count in (11, 111):
            end = "ов"
        else:
            end = ""
    elif count in nums:
        end = "а"
    else:
        end = "ов"

    return end

def put_to_cart(request, product):
    email = request.COOKIES["email"]
    pr = request.COOKIES["products"] + product + "|"
    resp = redirect("/get-user-data")
    resp.set_cookie("products", pr)
    acc = Account.objects.get(email=email)
    acc.user.products = pr
    acc.user.save(update_fields=["products"])
    return resp

def del_from_cart(request, product):
    email = request.COOKIES["email"]
    pr = request.COOKIES["products"]
    pr = pr.replace(f"{product}|", "")
    resp = redirect("/get-user-data")
    resp.set_cookie("products", pr)
    acc = Account.objects.get(email=email)
    acc.user.products = pr
    acc.user.save(update_fields=["products"])
    return resp

def videocards(request):
    pr = Product.objects.filter(type="Видеокарта")
    p = request.COOKIES["products"]
    count = len(pr)
    end = ""
    end2 = get_end(count)

    if end2 == "":
        end = ""
    else:
        end = "о"

    return render(request, "videocards.html", 
        {"pr": pr, "count": count, "end": end, "end2": end2, "p": p}
    )

def processors(request):
    pr = Product.objects.filter(type="Процессор")
    p = request.COOKIES["products"]
    count = len(pr)
    end = ""
    end2 = get_end(count)

    if end2 == "":
        end = ""
    else:
        end = "о"

    return render(request, "processors.html", 
        {"pr": pr, "count": count, "end": end, "end2": end2, "p": p}
    )