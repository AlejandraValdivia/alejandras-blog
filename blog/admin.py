from django.contrib import admin

from .models import Post, Comment, Author


class PostAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'date')
    list_display = ('title', 'slug', 'author', 'date', 'image')
    prepopulated_fields = {'slug': ('title',)}
    



admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)