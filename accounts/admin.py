from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
     list_display = ('email', 'is_staff','is_active' )
admin.site.register(CustomUser,CustomUserAdmin)
# Register your models here.
