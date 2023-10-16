from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'created_at', 'updated_at']
    # fields = ['title', 'content'] # 버전업되서 안된다.

admin.site.register(Post, PostAdmin)