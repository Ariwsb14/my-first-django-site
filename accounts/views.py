from django.shortcuts import render , redirect 
from django.contrib.auth import authenticate, login , logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import CustomUser
def login_view(request):
    if request.method == 'POST':
        try :
            reusername = request.POST["reusername"]
            reemail = request.POST["reemail"]
            repassword = request.POST["repassword"]
            user = CustomUser.objects.create_user(reusername, reemail, repassword)
            user.save()
            user = authenticate(request, username=reemail, password=repassword)
            login(request,user)
            return redirect('/') 
        except:
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('/')    
    return render(request , 'accounts/login-signup.html')

def forgotPass(request):
    return render(request , 'accounts/forgotpass.html')

def logout_view(request):   
   
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))

# Create your views here.
