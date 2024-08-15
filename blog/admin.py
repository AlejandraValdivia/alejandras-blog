from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Post, Comment, Author
import logging

logger = logging.getLogger(__name__)

class PostAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'date')
    list_display = ('title', 'slug', 'author', 'date', 'image')
    prepopulated_fields = {'slug': ('title',)}


    def save_model(self, request, obj, form, change):
        if not obj.author:
            author, created = Author.objects.get_or_create(username=request.user.username)
            obj.author = author
        obj.save()
        logger.info(f'Post "{obj.title}" saved by {obj.author.username}')


admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)