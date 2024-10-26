from django.shortcuts import render ,  get_object_or_404
from blog.models import Post
import datetime

def home(request):
    posts = Post.objects.filter(published_date__lte=datetime.datetime.now() , status=True)
    context = {'posts':posts}
    return render(request , 'blogs/blog-home.html' , context)   


def single(request,pid):
    post = get_object_or_404(Post, pk=pid, status=True)
    context = {'post':post}
    return render(request , 'blogs/blog-single.html', context)

# Create your views here.
