from ast import Return
from django.contrib import admin
from .models import Category, News
from django.utils.safestring import mark_safe

class NewыAdmin(admin.ModelAdmin):
    list_display=('id','title','category','created_at','updated_at','is_published','get_photo')
    list_display_links=('id','title')
    search_fields = ('title','content')
    list_editable=('is_published',)
    list_filter=('is_published','category')
    fields=('title','category','content','views','get_photo','is_published','updated_at','created_at')
    readonly_fields=('get_photo','views','updated_at','created_at')
    def get_photo(self,obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
    
    get_photo.short_description = 'миниатюра'

class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','title')
    list_display_links=('id','title')
    search_fields = ('title',)
     



admin.site.register(News,NewыAdmin)
admin.site.register(Category,CategoryAdmin)

admin.site.site_title='Управление новостями'
admin.site.site_header='Управление новостями'