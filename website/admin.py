from django.contrib import admin
from website.models import contact

class contactAdmin(admin.ModelAdmin):
    list_display = ['name' , 'email','created_date']
    date_hierarchy  = 'created_date'
    empty_value_display = '-empty-'
    search_fields = ['email','subject' , 'message']
    list_filter = ['email']

admin.site.register(contact,contactAdmin)

# Register your models here.
