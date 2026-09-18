"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , re_path
from home.views import *
from authentication.views import *
from election.views import *
from caPartice.views import *
from CA.views import * 
urlpatterns = [
    path('',home,name="home"),
    path('gret',gret,name="gret"),
    #its is dymnic url modification
    path('items/<str:menus>/',items,name="items"),
    path('checking',checking,name="checking"),
    #its is dynamic url with query parameter
    path('recipe/',recipe,name="recipe"),
    path('restaurant/',restaurant, name="restaurant"),
    path('cal/',cal,name="cal"),
    #its is handling optional paramters
    path('restro_detail/<str:category>[\w-]+/?<str:subcategory>[\w-]+/?',restro_detail, name="restro_detail"),
    path('login',login,name="login"),
    path('submit_data',submit_data,name="submit_data"),
    path('admin/', admin.site.urls),
    path('election',election,name = "election"),
    path('demo',demo,name = "demo"),
    path('students',students,name = "students"),
    path('exam/',exam,name="exam"),
    path('Exm/<str:subject>/',Exm, name="Exm"),
    path('student/<int:id>/',student, name="student"),
    path('per/',per, name="per"),
    re_path(r'^Hallticket/(?P<ticket>\d{6})/$',Hallticket,name="Hallticket"),



    #ca
    path('filter/',filter, name="filter"),

    path('movie/<str:genre>/', movie, name="movie"),
    path('screen/<int:id>/',screen, name = "screen"),
    re_path(r'^booking/(?P<booking_id>BK\d{4})/$',booking,name="booking"),
    path('search/',search,name="searching"),


]

