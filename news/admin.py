from django.contrib import admin
from news.models import News
from comments.models import Comment

#admin.site.register(News)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'category']
    list_filter = ('category',)

@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['author', 'written_on']
    
