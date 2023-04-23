# from django.contrib.auth import get_user_model
from rest_framework import serializers

from user.models import User
from user.serializers import UserSerializer


from socialmedia.models import Profile, Post, Comment


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("id", "user", "profile_picture", "followers")


class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("id", "profile_picture")


class ProfileDetailSerializer(ProfileSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = (
            "id",
            "user",
            "bio",
            "followers",
            "profile_picture",
        )


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ("id", "user", "content", "image", "created_at", "likes")


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ("id", "user", "post", "content", "created_at")


class UserSearchSerializer(serializers.Serializer):
    search = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ("id", "user")
