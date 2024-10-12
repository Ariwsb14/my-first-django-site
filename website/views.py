from django.shortcuts import render

from django.http import HttpResponse


def first_text(request):
    return render(request , 'index.html')
# Create your views here.
