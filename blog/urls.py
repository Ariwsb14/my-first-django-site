from blog.views import *
from django.urls import path 

app_name = 'blog'
urlpatterns = [

    path('', home , name='index'),
    path('<int:pid>', single , name='single'),
    path('category/<str:cat_name>', home , name='category'),

]
