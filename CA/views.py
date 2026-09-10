from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#question3
# http://127.0.0.1:/8000/filter/?genre=action&year=2025

def filter(request):
    genre = request.GET.get('genre',"none of them")
    year = request.GET.get('year',00000)

    return HttpResponse (f"the movie genre {genre} and year is {year}")

#question4
#a
def movie(request,genre):
    return HttpResponse(f"The movie genre is {genre}")

#b
def screen(request,id):
    return HttpResponse(f"this screen size is : {id}")

#c
#/booking/BK4587/
def booking(request,booking_id):
    return HttpResponse(f"the booking id is : {booking_id}")

#d
#/searching/?city=delhi&date=15
def search(request):
    city2 = request.GET.get('city2', "non "),
    date = request.GET.get('date',99-99-99)
    return HttpResponse(f"the city is : {city2} and date is : {date}")