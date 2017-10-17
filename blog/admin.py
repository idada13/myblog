from django.contrib import admin

from .models import Post, Comment

# customise the Admin interface
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_date']
    list_filter = ['published_date']

# update the registration to include our customised interface
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
