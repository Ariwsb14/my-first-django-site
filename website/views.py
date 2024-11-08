from django.shortcuts import render
from website.forms import ContactForm
from django.http import HttpResponse


def index(request):
    return render(request , 'website/index.html')

def about(request):
    return render(request , 'website/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            
    form = ContactForm()
    return render(request , 'website/contact.html', {'form':form})

def elements(request):
    return render(request , 'website/elements.html')
# Create your views here.
