from website.models import contact
from django.forms import ModelForm

class ContactForm(ModelForm):
    class Meta:
        model = contact
        fields = '__all__'

