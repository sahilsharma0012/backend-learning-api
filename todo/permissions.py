from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        
        # Allow everyone to read
        if request.method == 'GET':
            return True
        
        # Only admin for create/update/delete
        return request.user.is_staff