from django.contrib import admin
from website.models import contact , newsletter

class contactAdmin(admin.ModelAdmin):
    list_display = ['name' , 'email','created_date']
    date_hierarchy  = 'created_date'
    empty_value_display = '-empty-'
    search_fields = ['email','subject' , 'message']
    list_filter = ['email']



class newsadmin(admin.ModelAdmin):
    list_display = ['email']

admin.site.register(contact,contactAdmin)
admin.site.register(newsletter , newsadmin)    

# Register your models here.
