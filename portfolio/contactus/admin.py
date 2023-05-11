from django.contrib import admin
from django.contrib.admin import AdminSite

from . import models
# Register your models here.

class Contactkarsala(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'


admin.site.register(models.ContactUs)
admin.site.site_header  =  "Admin Panel | Viral Sachde"
admin.site.site_title  =  "Admin Panel | Viral Sachde"
admin.site.index_title  =  "Admin Panel | Viral Sachde"