from django import template
from blog.models import Post , category

register = template.Library()
@register.inclusion_tag('blogs/sidebar-categories.html')
def sidebar_categories():
    posts =  Post.objects.filter(status=True)
    categories = category.objects.all()
    cats_count = dict()
    for cat in categories:
        cats_count[cat] = posts.filter(category=cat).count()

    return {'categories':cats_count}    