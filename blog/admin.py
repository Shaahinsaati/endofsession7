from django.contrib import admin
from blog.models import Post,Category #,Tag
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empyt_value_display ='-empty-'
    list_display = ('title','author','image','counted_views','status','published_date','created_date')
    list_filter = ('status','author','counted_views')
    # ordering = ['created_date']
    search_fields = ('title','content')
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
# admin.site.register(Tag)
