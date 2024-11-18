from django.shortcuts import render
from website.forms import ContactForm , newsform
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

def newsletter(request):
    if request.method == 'POST':
        form = newsform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request , message='form saved successfully')
        else:
            messages.error(request , message='please enter a valid values for the form')  
    return render(request , 'website/index.html')
# Create your views here.
