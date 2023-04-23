from django.urls import path, include
from rest_framework import routers

from socialmedia.views import (
    ProfileViewSet,
    PostViewSet,
    CommentViewSet,
    UserSearchView,
)


router = routers.DefaultRouter()
router.register(r"profiles", ProfileViewSet)
router.register(r"posts", PostViewSet)
router.register(r"comments", CommentViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "profiles/<int:pk>/update-profile/",
        ProfileViewSet.as_view({"put": "update_profile"}),
        name="update-profile",
    ),
    path("users/search/", UserSearchView.as_view(), name="user-search"),
]

app_name = "socialmedia"
