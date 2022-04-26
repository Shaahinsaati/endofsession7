from django.contrib import admin
from django.urls import path
from blog.views import *
from django.conf.urls.static import static
from django.conf import settings


app_name = 'blog'

urlpatterns = [
    path('', blog_home,name='blog_home'),
    path('<int:pid>', blog_single,name='blog_single'),
    path('category/<str:cat_name>' ,blog_home,name='category'),
    path('author/<str:author_username>' ,blog_home,name='author'),
    path('search/' ,blog_search,name='search'),
    path('test/',test,name='test'),
    
]
