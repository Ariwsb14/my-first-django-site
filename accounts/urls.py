from django.urls import path 
from accounts.views import login_view , forgotPass , logout_view

app_name = 'accounts'

urlpatterns = [
    path('login' , login_view ,name='login'),
    path('forgot-pass', forgotPass , name ='forgot-pass'),
    path('logout', logout_view , name ='logout'),
]