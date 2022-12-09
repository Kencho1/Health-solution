from django.contrib import admin
from .models import Post,Comment


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display =('title','content','date_posted','author')

admin.site.register(Post,PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display =('post','author','content','data_added')

admin.site.register(Comment,CommentAdmin)