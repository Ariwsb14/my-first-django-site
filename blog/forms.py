from blog.models import Comments
from django.forms import ModelForm

class commentform(ModelForm):
    class Meta:
        model = Comments
        fields = ['post' , 'name' , 'email', 'subject', 'message']