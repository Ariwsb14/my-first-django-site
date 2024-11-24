from django.shortcuts import render ,  get_object_or_404
from blog.models import Post , Comments 
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
import datetime
from blog.forms import commentform
from django.contrib import messages

def home(request,cat_name=None, tag_name=None):
    posts = Post.objects.filter(published_date__lte=datetime.datetime.now() , status=True)
    pop_posts = sorted(posts, key=lambda x: x.counted_view, reverse=True)
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    if tag_name:
        posts = posts.filter(tags__name__in=[tag_name])            
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
    comments = Comments.objects.filter(post = pid, approved = True)
    post = get_object_or_404(Post, pk=pid, status=True)
    #counting views
    post.counted_view += 1
    post.save() 
    #end of counting views

    # cooments form
    if request.method == 'POST':
        form = commentform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request , message='form has been successfuly sent')
        else:
            messages.error(request, message='please fill the form corectly')    
    form = commentform()           

    



    # next and previous posts
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
    # end of next and previous posts
    pop_posts = sorted(posts, key=lambda x: x.counted_view, reverse=True)  
         
    context = {'post':post , 'index':index , 'perv': perv , 'next': next , 'pop_posts':pop_posts , 'comments':comments , 'form':form }
    return render(request , 'blogs/blog-single.html', context)

def search(request):
    posts = Post.objects.filter(published_date__lte=datetime.datetime.now(),status=True)
    if request.method == 'GET':
         if s:= request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts':posts}
    return render(request , 'blogs/blog-home.html' , context )
# Create your views here.
