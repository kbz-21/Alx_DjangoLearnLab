from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission: only owners can edit/delete. Read allowed for all.
    """

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS (GET, HEAD, OPTIONS) are allowed
        if request.method in permissions.SAFE_METHODS:
            return True
        # Otherwise, check ownership (post.author for Post, comment.author for Comment)
        return getattr(obj, 'author', None) == request.user
