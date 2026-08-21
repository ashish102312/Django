from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, "home.html")

def checking(request):
    return render(request,"check.html")


def gret(request):
    return HttpResponse("<h1>this is greeting from my side</h1>")

def items(request):
    # return HttpResponse("list of items")
    items = {
        "pizza" : {"name" : "Pizza", "price":400},
        "burger" : {"name" : "veg burger", "price": 70},
        "noodles" : {"name" : "non-veg noodles","price" : 300}
    }
    return HttpResponse(str(items))