from django.contrib import admin
from .models import BlogPost, BlogContent, contact_detail

class BlogContentInline(admin.StackedInline):
    model = BlogContent
    extra = 1

class BlogPostAdmin(admin.ModelAdmin):
    inlines = [BlogContentInline]
    list_display = ('title', 'category', 'author', 'display_image')
    search_fields = ['title', 'category', 'author']

    def display_image(self, obj):
        return '<img src="{}" width="50" height="50" />'.format(obj.image.url)

    display_image.allow_tags = True
    display_image.short_description = 'Image'

admin.site.register(BlogPost, BlogPostAdmin)

admin.site.register(contact_detail)