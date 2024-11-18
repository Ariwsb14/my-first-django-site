from website.models import contact , newsletter
from django.forms import ModelForm

class ContactForm(ModelForm):
    class Meta:
        model = contact
        
        fields = '__all__'

class newsform(ModelForm):
    class Meta:
        model = newsletter
        fields = '__all__'


    
        

