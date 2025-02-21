from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin

from .models import *


admin.site.site_header = _('Administração de ZooUnama')
admin.site.index_title = _('ZooUnama')


@admin.register(Animal)
class AnimaisAdmin(TranslationAdmin):
    ordering = ['name']
    list_display = ["__str__", "scientific_name", "created_by", "created_at", "updated_by", "updated_at"]
    list_filter = ['type']
    search_fields = ['name', 'scientific_name']

    def save_model(self, request, obj, form, change):
        if not obj.pk:  
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()
        super().save_model(request, obj, form, change)

class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1


@admin.register(Post)
class PostAdmin(TranslationAdmin):
    ordering = ['title']
    list_display = ['title', 'place', 'created_by', 'created_at', 'updated_by', 'updated_at']
    list_filter = ['place']
    search_fields = ['title', 'description']
    inlines = [PostImageInline]

    def save_model(self, request, obj, form, change):
        if not obj.pk:  
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()
        super().save_model(request, obj, form, change)

    


@admin.register(Notice)
class EditaisAdmin(TranslationAdmin):
    ordering = ['title']
    list_display = ['title', 'created_by', 'created_at', 'updated_by', 'updated_at']
    def save_model(self, request, obj, form, change):
        if not obj.pk:  
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()
        super().save_model(request, obj, form, change)