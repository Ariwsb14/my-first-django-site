from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

class category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    image = models.ImageField(upload_to='blog/' , default='media/blog/default.jpg')
    author = models.ForeignKey(User, on_delete=models.SET_NULL , null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ManyToManyField(category)
    counted_view = models.IntegerField(default=0)
    tags = TaggableManager()
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta :
        ordering = ['-created_date']
    def __str__(self):
        return '%s - %s' % (self.id , self.title) 

    def get_absolute_url(self):
        return reverse('blog:single', kwargs={'pid':self.id}) 

class coment(models.Model):
    post = models.ForeignKey(Post , on_delete= models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()  
    subject = models.CharField(max_length=255)
    message = models.TextField() 
    status = models.BooleanField(default= False) 
    created_date = models.DateTimeField(auto_now_add= True)
    published_date = models.DateTimeField(auto_now= True)

    def __str__(self) :
        return  '%s - %s'% (self.post , self.name)
    



# Create your models here.
