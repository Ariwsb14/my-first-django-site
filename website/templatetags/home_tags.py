from django import template
from blog.models import Post
import datetime

register = template.Library()

@register.inclusion_tag('website/home-lastposts.html')
def lastposts():
    posts = Post.objects.filter(status=True , published_date__lte=datetime.datetime.now())
    last_posts  = sorted(posts, key=lambda x: x.published_date , reverse=True)[:6]
    return {'lastposts':last_posts}


