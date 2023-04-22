import os
import uuid

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _
from user.models import User
from django.utils.text import slugify


def create_custom_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.title)}-{uuid.uuid4()}{extension}"
    return os.path.join("uploads/movies/", filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=300, blank=True)
    profile_picture = models.ImageField(upload_to='create_custom_path', null=True, blank=True)
    # profile_picture = models.ImageField(null=True, upload_to="uploads/")
    followers = models.ManyToManyField(User, related_name='following', blank=True)

    def __str__(self):
        return self.user.username


# class Post(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()
#     image = models.ImageField(upload_to='post_images', blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
#
#     def __str__(self):
#         return f'{self.user.username} - {self.content[:20]}'
#
#     class Meta:
#         ordering = ['-created_at']
#
#
# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'{self.user.username} - {self.content[:20]}'
#
#     class Meta:
#         ordering = ['created_at']