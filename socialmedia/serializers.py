# from django.contrib.auth import get_user_model
from rest_framework import serializers
from user.serializers import UserSerializer


# from socialmedia.models import Profile, Post, Comment
from socialmedia.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'user', 'bio', 'profile_picture', 'followers')


class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("id", "profile_picture")


class ProfileDetailSerializer(ProfileSerializer):
    # genres = GenreSerializer(many=True, read_only=True)
    # actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = (
            "id",
            "user",
            "bio",
            "followers",
            "profile_picture",
        )

# class PostSerializer(serializers.ModelSerializer):
#     user = UserSerializer(read_only=True)
#     likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#
#     class Meta:
#         model = Post
#         fields = ('id', 'user', 'content', 'image', 'created_at', 'likes')
#
#
# class CommentSerializer(serializers.ModelSerializer):
#     user = UserSerializer(read_only=True)
#
#     class Meta:
#         model = Comment
#         fields = ('id', 'user', 'post', 'content', 'created_at')

