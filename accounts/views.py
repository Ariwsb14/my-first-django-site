from django.shortcuts import render

def login(request): 
    return render(request , 'accounts/login-signup.html')

def forgotPass(request):
    return render(request , 'accounts/forgotpass.html')

# Create your views here.
