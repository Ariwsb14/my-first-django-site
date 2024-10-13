from .views import *
from django.urls import path 

urlpatterns = [

    path('',index),
    path('about', about),
    path('contact', contact),
    path('elements' , elements)

]
