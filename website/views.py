from django.shortcuts import render

from django.http import HttpResponse


def first_text(request):
    return HttpResponse('hello world')
# Create your views here.
