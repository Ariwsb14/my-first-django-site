from django.shortcuts import render ,  get_object_or_404
from blog.models import Post
import datetime

def home(request):
    posts = Post.objects.filter(published_date__lte=datetime.datetime.now() , status=True)
    context = {'posts':posts}
    return render(request , 'blogs/blog-home.html' , context)   


def single(request,pid):
    posts = Post.objects.filter(published_date__lte=datetime.datetime.now(),status=True)
    post = get_object_or_404(Post, pk=pid, status=True)
    index = 0
    for i in range(len(posts)):
        if posts[i].id == post.id:
            index = i

    tedad = len(posts)
    perv = None
    if index+2 <= tedad:
        perv = posts[index+1]
    else:
        None  

    next = None
    if index > 0:
        next = posts[index-1]
    else:
        None    
         
        
    
    
        
    
    context = {'post':post , 'index':index , 'perv': perv , 'next':next }
    return render(request , 'blogs/blog-single.html', context)

# Create your views here.
