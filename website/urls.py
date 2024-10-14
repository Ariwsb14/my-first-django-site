from .views import *
from django.urls import path 

app_name = 'website'
urlpatterns = [

    path('',index , name='index'),
    path('about', about , name='about'),
    path('contact', contact , name='contact'),
    path('elements' , elements , name='elements')

]
