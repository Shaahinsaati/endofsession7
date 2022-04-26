from django.contrib import admin
from website.models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name','email','subject','created_date')
    list_filter = ['email','subject','created_date']
    search_fields = ('name','email','subject','created_date')
admin.site.register(Contact,ContactAdmin)