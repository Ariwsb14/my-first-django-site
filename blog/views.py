from django.shortcuts import render ,  get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
import datetime

def home(request,cat_name=None):
    posts = Post.objects.filter(published_date__lte=datetime.datetime.now() , status=True)
    pop_posts = sorted(posts, key=lambda x: x.counted_view, reverse=True)
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    posts = Paginator(posts,3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)    
    except PageNotAnInteger:
        posts = posts.get_page(1) 
    except EmptyPage:
        posts = posts.get_page(1) 
    context = {'posts':posts , 'pop_posts':pop_posts }
    return render(request , 'blogs/blog-home.html' , context)   


def single(request,pid):
    posts = Post.objects.filter(published_date__lte=datetime.datetime.now(),status=True)
    post = get_object_or_404(Post, pk=pid, status=True)
    post.counted_view += 1
    post.save() 
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

    pop_posts = sorted(posts, key=lambda x: x.counted_view, reverse=True)  
         
    context = {'post':post , 'index':index , 'perv': perv , 'next': next , 'pop_posts':pop_posts }
    return render(request , 'blogs/blog-single.html', context)

def search(request):
    posts = Post.objects.filter(published_date__lte=datetime.datetime.now(),status=True)
    if request.method == 'GET':
         if s:= request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts':posts}
    return render(request , 'blogs/blog-home.html' , context )
# Create your views here.
