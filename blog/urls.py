from blog.views import *
from django.urls import path 

app_name = 'blog'
urlpatterns = [

    path('', home , name='index'),
    path('single', single , name='single'),
    

]
