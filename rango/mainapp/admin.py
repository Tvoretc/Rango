from django.contrib import admin
from mainapp.models import Category, Page, UserProfile

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Category._meta.fields if f.name not in ['views', 'likes', 'slug']]

admin.site.register(Category, CategoryAdmin)

class PageAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Page._meta.fields if f.name not in ['views', 'likes', 'slug']]

admin.site.register(Page, PageAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = [f.name for f in UserProfile._meta.fields]

admin.site.register(UserProfile, ProfileAdmin)
