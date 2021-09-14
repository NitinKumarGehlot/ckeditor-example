from django.conf.urls import url
from django.urls import path,include
from . import views

urlpatterns = [
    path('add/',views.index,name="home_page"),
    path('',views.show,name="show_data")

] 
