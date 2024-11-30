from django.urls import path 
from accounts.views import login , forgotPass

app_name = 'accounts'

urlpatterns = [
    path('login' , login ,name='login'),
    path('forgot-pass', forgotPass , name ='forgot-pass'),
]