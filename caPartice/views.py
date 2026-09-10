from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def exam(request):
    subject = request.GET.get('subject', "No subject found")
    duration = request.GET.get('duration', 0)
    return HttpResponse(f'subject is {subject} and the duration is {duration} min')

def Exm(request,subject):
    return HttpResponse(f'subject is {subject} ')

def student(request,id):
    return HttpResponse(f"student id is {id}")

def per(request):
    roll = request.GET.get('roll', "no roll number")
    sem = request.GET.get('sem',1)
    return HttpResponse(f'the roll is ={roll}, the sem is= {sem}')

def Hallticket(request,ticket):
    return HttpResponse(f"the hallticket is: {ticket}")