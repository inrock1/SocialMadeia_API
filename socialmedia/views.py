from rest_framework import viewsets, status, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from user.models import User
from user.serializers import UserSerializer
from .models import Profile, Post, Comment
from .serializers import (
    ProfileSerializer,
    ProfileImageSerializer,
    ProfileDetailSerializer,
    PostSerializer,
    CommentSerializer,
)
from .permissions import IsOwnerOrReadOnly


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(
        methods=["POST"],
        detail=True,
        url_path="upload-image",
        permission_classes=[IsOwnerOrReadOnly],
    )
    def upload_image(self, request, pk=None):
        profile = self.get_object()
        serializer = self.get_serializer(profile, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):

        if self.action == "retrieve":
            return ProfileDetailSerializer

        if self.action == "upload_image":
            return ProfileImageSerializer

        return ProfileSerializer

    @action(methods=["put"], detail=True, url_path="update-profile")
    def update_profile(self, request, pk=None):
        profile = self.get_object()
        serializer = ProfileDetailSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["get"])
    def followers(self, request, pk=None):
        profile = self.get_object()
        followers = profile.followers.all()
        serializer = ProfileSerializer(followers, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def following(self, request, pk=None):
        profile = self.get_object()
        following = profile.following.all()
        serializer = UserSerializer(following, many=True)
        return Response(serializer.data)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=["post"])
    def like(self, request, pk=None):
        post = self.get_object()
        post.likes.add(request.user)
        return Response({"status": "liked"})

    @action(detail=True, methods=["post"])
    def unlike(self, request, pk=None):
        post = self.get_object()
        post.likes.remove(request.user)
        return Response({"status": "unliked"})


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserSearchView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        query = self.request.query_params.get("search")
        qs = User.objects.all()
        if query:
            qs = qs.filter(username__icontains=query)
        return qs
