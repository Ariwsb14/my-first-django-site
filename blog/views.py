from django.shortcuts import render
from blog.models import Post
import datetime

def home(request):
    posts = Post.objects.filter(published_date__lte=datetime.datetime.now() , status=True)
    context = {'posts':posts}
    return render(request , 'blogs/blog-home.html' , context)   


def single(request):
    return render(request , 'blogs/blog-single.html')

# Create your views here.
