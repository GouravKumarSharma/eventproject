from django.contrib import admin
from django.urls import path
from upasanaapp import views


urlpatterns = [

    path('', views.index, name='index'),
    path('gellery',views.gellery,name='gellery'),
    path('about',views.about,name="about"),
    path('contact',views.contect,name="contect"),
    path('videosgellery',views.videosgellery,name="videosgellery"),

]
