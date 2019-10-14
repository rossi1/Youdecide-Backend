from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Custom of class IsOwnerOrReadOnly(permissions.BasePermission)
    That an APIexception is raised instead
    We do not want a ReadOnly
    """

    def has_object_permission(self, request, view, obj):

        # First check if authentication is True
        permission_classes = (permissions.IsAuthenticated, )
        # Instance is the user
        return obj.id == request.user.id