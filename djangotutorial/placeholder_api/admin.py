from django.contrib import admin

from .models import Comment, User, Todo, Album, Photo, Post

admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Todo)
admin.site.register(Album)
admin.site.register(Photo)
admin.site.register(Post)
