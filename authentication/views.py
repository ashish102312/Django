from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def login(request):
    return render(request,"from.html")

def submit_data(request):
    if request.method =='POST':
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        phone= request.POST.get("phone")
        gender=request.POST.get("gender")
        return HttpResponse(f'<h1>full name:{first_name + last_name}</h1><p>your email is: {email} </p><p>your phone number is: {phone}</p><p>your gender is: {gender}</p>')
    return HttpResponse("<h2>first login in you will see this page </h2>")
        
