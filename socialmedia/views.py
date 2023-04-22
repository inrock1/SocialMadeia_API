# from django.shortcuts import render
# from rest_framework import viewsets, mixins, status, generics
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from .models import Profile, Post, Comment
# from .serializers import UserSerializer, ProfileSerializer, PostSerializer, CommentSerializer
# from .permissions import IsOwnerOrReadOnly


# class ProfileViewSet(viewsets.ModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#
#     @action(detail=True, methods=['get'])
#     def followers(self, request, pk=None):
#         profile = self.get_object()
#         followers = profile.followers.all()
#         serializer = UserSerializer(followers, many=True)
#         return Response(serializer.data)
#
#     @action(detail=True, methods=['get'])
#     def following(self, request, pk=None):
#         profile = self.get_object()
#         following = profile.following.all()
#         serializer = UserSerializer(following, many=True)
#         return Response(serializer.data)
#
#
# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#
#     @action(detail=True, methods=['post'])
#     def like(self, request, pk=None):
#         post = self.get_object()
#         post.likes.add(request.user)
#         return Response({'status': 'liked'})
#
#     @action(detail=True, methods=['post'])
#     def unlike(self, request, pk=None):
#         post = self.get_object()
#         post.likes.remove(request.user)
#         return Response({'status': 'unliked'})
#
#
# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
