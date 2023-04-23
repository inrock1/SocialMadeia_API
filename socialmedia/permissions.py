from rest_framework import permissions

from socialmedia.models import Profile


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the object being accessed is a user profile object
        if isinstance(obj, Profile):
            # Only allow owners of the profile to edit it
            return obj.user == request.user

        # For non-user profile objects, allow safe methods (e.g. GET) for everyone
        # and write methods (e.g. POST, PUT, DELETE) only for authenticated users
        return (
            request.method in permissions.SAFE_METHODS or request.user.is_authenticated
        )
