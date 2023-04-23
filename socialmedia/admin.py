from django.contrib import admin

from socialmedia.models import Post, Comment, Profile


admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
