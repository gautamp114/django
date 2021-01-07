from django.contrib import admin

from .models import Post, Comment, Following

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'date_posted', 'caption']

    readonly_fields = ['date_posted']

    class Meta:
        model = Post
        
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'content', 'comment_date']

    class Meta:
        model = Comment




admin.site.register(Post,PostAdmin)

admin.site.register(Comment,CommentAdmin)

admin.site.register(Following)