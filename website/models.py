from django.db import models

class contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255 ,default=None , null=True , blank=True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_date']
    def __str__(self):  
        return '%s - %s' % (self.id , self.name)
    
class newsletter(models.Model):
    email = models.EmailField() 
    def __str__(self):
        return '%s - %s ' % (self.id , self.email)   
# Create your models here.
