from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
def home(request):
    return render(request, "home.html")

def checking(request):
    return render(request,"check.html")


def gret(request):
    return HttpResponse("<h1>this is greeting from my side</h1>")


menu = {
        "pizza" : {"name" : "Pizza", "price":400},
        "burger" : {"name" : "veg burger", "price": 70},
        "noodles" : {"name" : "non-veg noodles","price" : 300}
    }

def items(request,menus):
    # return HttpResponse("list of items")
    if menus in menu:
        data = menu[menus]
        return HttpResponse(f"{data['name']} cost Rs {data['price']}")
    else:
        return HttpResponse("Item is not found")