from rest_framework import permissions


class IsAuthorOrAdminOrModerator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        role = ('admin', 'moderator')
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method == 'POST':
            return request.user.is_authenticated 
        elif request.method in ('PUT', 'PATCH', 'DELETE'):
            return (request.user.role in role) or obj.author == request.user or request.user.is_staff
      