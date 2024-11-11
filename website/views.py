from django.shortcuts import render
from website.forms import ContactForm
from django.http import HttpResponse
from django.contrib import messages


def index(request):
    return render(request , 'website/index.html')

def about(request):
    return render(request , 'website/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.instance.name = 'anonymous'
            form.save()
            messages.success(request , message='form has been successfuly sent')
        else:
            messages.error(request, 'please fill the form corectly')    
            
    form = ContactForm()
    return render(request , 'website/contact.html', {'form':form})

def elements(request):
    return render(request , 'website/elements.html')
# Create your views here.
