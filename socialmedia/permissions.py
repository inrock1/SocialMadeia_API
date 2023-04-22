# from rest_framework.permissions import SAFE_METHODS, BasePermission


# class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
#     def has_permission(self, request, view):
#         return bool(
#             (
#                 request.method in SAFE_METHODS
#                 and request.user
#                 and request.user.is_authenticated
#             )
#             or (request.user and request.user.is_staff)
#         )


from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the object.
        return obj.owner == request.user
