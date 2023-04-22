from django.urls import path, include
from rest_framework import routers

from socialmedia.views import (
    ProfileViewSet, PostViewSet,
)


router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [path('', include(router.urls))]

app_name = "socialmedia"


# from socialmedia.views import (
#     UserViewSet,
#     ProfileViewSet,
#     PostViewSet,
#     CommentViewSet
# )

# router.register(r'users', UserViewSet)
# router.register(r'comments', CommentViewSet)