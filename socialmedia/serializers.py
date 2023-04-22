# from django.contrib.auth import get_user_model
# from rest_framework import serializers

# from socialmedia.models import Profile, Post, Comment







# class ProfileSerializer(serializers.ModelSerializer):
#     user = UserSerializer(read_only=True)
#
#     class Meta:
#         model = Profile
#         fields = ('id', 'user', 'bio', 'profile_picture', 'followers')
#
#
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

