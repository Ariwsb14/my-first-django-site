from django.contrib import admin

from blog.models import Post , category , Comments

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'status','author' , 'created_date', 'published_date')
    list_filter = ('status', 'author')
    search_fields = ('title', 'content', )

class CommentsAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name', 'approved','post')
    search_fields = ('name' , 'post' , 'subject')
    list_filter =( 'name' , 'post') 

admin.site.register(Post,PostAdmin)
admin.site.register(category)    
admin.site.register(Comments,CommentsAdmin)
# Register your models here.
