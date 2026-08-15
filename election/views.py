from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def election(request):
    return render(request,"election-check.html",{"voters":voter})
voter = [{"name":"amit","age":23},
           {"name":"ashish","age":21},
           {"name":"rahul","age":23},
           {"name":"anuksh","age":17},
           {"name":"rohit","age":18},
           {"name":"sachin","age":34},
]
