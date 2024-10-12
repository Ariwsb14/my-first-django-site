from .views import first_text
from django.urls import path 

urlpatterns = [

    path('',first_text)

]
