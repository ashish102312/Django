from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def election(request):
    return render(request,"election-check.html",{"voters":voter})
voter = [{"name":"amit","age":23,"gender":"male"},
           {"name":"ashish","age":21,"gender":"male"},
           {"name":"rahul","age":23,"gender":"male"},
           {"name":"anuksh","age":17,"gender":"male"},
           {"name":"rohit","age":18,"gender":"male"},
           {"name":"sachin","age":34,"gender":"male"},
           {"name":"sakshi","age":25,"gender":"female"},
]

def demo(request):
    return render(request,"demo.html",{"details" :detail})
detail = [{
    "name": "Rahul",
    "Course": "python",
    "city" : "Delhi",
    "studetns" :["Rohit","Ramesh","Suresh"]
}]
