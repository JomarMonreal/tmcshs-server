# permissions.py
from rest_framework.permissions import BasePermission


class IsSuperAdminForNonGetMethods(BasePermission):
    def has_permission(self, request, view):
        # Allow GET and HEAD methods for everyone
        if request.method in ['GET', 'POST']:
            return True

        # Restrict other methods to super admins only
        return request.user and request.user.is_superuser
