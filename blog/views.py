from pickle import NONE
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from blog.models import Post
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


def blog_home(request,**kwargs):
    posts = Post.objects.filter(status=1,published_date__lte = timezone.now())
    #kwargs to find out what type of request we get and what to do for each one
    if kwargs.get('cat_name') !=None:
        posts=posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') !=None:
        posts = posts.filter(author__Username=kwargs['author_username'])
    #pagination down here
    posts = Paginator(posts,3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.page(posts.num_pages)
    context = {'posts': posts,'page':page_number}
    return render(request,'blog/blog-home.html',context)


def blog_single(request,pid):
    post = get_object_or_404(Post, pk=pid, status=1)
    post.counted_views = post.counted_views +1
    post.save()

    posts_list = Post.objects.filter(status=1,published_date__lte = timezone.now()).order_by('id')

    for index, this_post in enumerate(posts_list):
        if this_post.id == post.id:
            index_of_current_post = index

    context = {
        'post': post,
        'next_post': None,
        'prev_post': None,
    }

    try:
        context['next_post'] = posts_list[index_of_current_post+1]
    except: pass

    try:
        context['prev_post'] = posts_list[index_of_current_post-1]
    except: pass
    
    return render(request,'blog/blog-single.html',context)

def test(request):
    if request.method == 'POST':
       print(request.POST.get('name'))
    


    return render(request,'blog/test.html')


def blog_search(request):
    posts = Post.objects.filter(status=1,published_date__lte = timezone.now())
    if request.method == 'GET':
        if s:=request.GET.get('s'):
            posts = posts.filter(content__contains = s)
        # elif s:= request.GET.get('s'):
        #     posts = posts.filter(title__contains = s)
    context = {'posts': posts}
    return render(request,'blog/blog-home.html',context)
