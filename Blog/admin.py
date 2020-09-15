from django.contrib import admin
from Blog.models import Topic, Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    list_filter = ('topic', 'author')
    readonly_fields = ('view', 'upvote', 'date')
    fieldsets = (
        ('Blog', {'fields': ('title', 'author', 'topic', 'body')}),
        ('Readonly', {'fields': ('view', 'upvote')}),
    )

admin.site.register(Topic)