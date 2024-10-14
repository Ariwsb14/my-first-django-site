from django.shortcuts import render


def home(request):
    return render(request , 'blogs/blog-home.html')

def single(request):
    return render(request , 'blogs/blog-single.html')

# Create your views here.
