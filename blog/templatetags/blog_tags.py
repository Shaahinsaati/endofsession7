from django import template
from blog.models import Post,Category
from django.utils import timezone


register = template.Library()

@register.simple_tag
def function():
    numberOfPosts = Post.objects.filter(status=1,published_date__lte=timezone.now()).count()
    return numberOfPosts

@register.filter
def snippet(value,arg=20):
    return value[:arg] + " ..."

@register.inclusion_tag('blog/blog-popularpostwidget.html')
def popularposts(arg=4):
    posts = Post.objects.filter(status=1,published_date__lte=timezone.now()).order_by('-counted_views')[:arg]
    return {'posts': posts}

@register.inclusion_tag('blog/blog-postcategorywidget.html')
def postcategories():
    posts = Post.objects.filter(status=1,published_date__lte=timezone.now())
    category = Category.objects.all()
    cat_dict = {}
    for name in category:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories':cat_dict}

# @register.inclusion_tag('blog/blog-postcategorywidget.html')
# def posttags():
#     posts = Post.objects.filter(status=1,published_date__lte=timezone.now())
#     tags = Tags.objects.all()
#     cat_dict = {}
#     for name in Tags:
#         cat_dict[name] = posts.filter(category=name).count()
#     return {'categories':cat_dict}