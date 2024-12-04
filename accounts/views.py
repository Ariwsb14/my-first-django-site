from django.shortcuts import render , redirect 
from django.contrib.auth import authenticate, login , logout
from django.urls import reverse
from django.http import HttpResponseRedirect
def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')

        else:
            authenticate(request, email=username, password=password)
            if user is not None:
                login(user) 
    return render(request , 'accounts/login-signup.html')

def forgotPass(request):
    return render(request , 'accounts/forgotpass.html')

def logout_view(request):   
   
    logout(request)
    return HttpResponseRedirect(reverse('website:index'))

# Create your views here.
