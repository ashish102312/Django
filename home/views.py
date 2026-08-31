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

food = {
        "pizza" : {"name" : "Pizza", "price":400},
        "burger" : {"name" : "veg burger", "price": 70},
        "noodles" : {"name" : "non-veg noodles","price" : 300}
    }

res = {
    "rest1" : {"name" : "JWM", "location" : "Sector 17" , "price": 200},
    "rest2" : {"name" : "MOONV+BLUE","location": "Sector 20", "price": 200},
    "rest3" : {"name" : "YELLOW FLASH", "location" : "Sector 30", "price": 200},
    
}

def items(request,menus):
    # return HttpResponse("list of items")
    if menus in menu:
        data = menu[menus]
        return HttpResponse(f"{data['name']} cost Rs {data['price']}")
    else:
        return HttpResponse("Item is not found")


#dynamic routing with models
def recipe(request):
    food = request.GET.get('items', 'No items found')
    quantity = request.GET.get('quantity', 1)
    price = request.GET.get('price',100)
    return HttpResponse(f"Your order: {quantity} of {food} with estimated price {price}")

def restaurant(request):
    res=request.GET.get('res',"NO avable RESTUARNT")
    name = request.GET.get('name')
    location = request.GET.get('location')
    price = request.GET.get('price')
    return HttpResponse(f"<h1>Searching....</h1><br><h2>Your selected resturent: {name}</h2><h2>The location is : {location}</h2><h2>and its price: {price}</h2>")

def cal(request):
    # Use .get() with a default of 0 to avoid int(None) errors
    value1 = int(request.GET.get('value1', 0))
    value2 = int(request.GET.get('value2', 0))
    sign = request.GET.get('sign')
    if sign == "+":
        return HttpResponse(f"The sum of {value1} and {value2} is {value1 + value2}")
    elif sign == "-":
        return HttpResponse(f"value1 = {value1} and the value {value2} ans will be {value1 - value2}")
    elif sign == "*":
        return HttpResponse(f"value1 = {value1} and the value {value2} ans will be {value1 * value2}")
    elif sign == "/":
        return HttpResponse(f"value1 = {value1} and the value {value2} ans will be {value1 / value2}")
    else:
        return HttpResponse("invalid operator. Please provide a valid sign (+, -, *, /)")
    
#handling optional paramters
def restro_detail(request,category,subcategory):
    #handle the case when subcategory is not provided
    if not subcategory:
        message  = f"showing all items in {category}"
    else:
        #subcategory provided
        message = f"showing {subcategory} -> {category}"
    return HttpResponse(message)