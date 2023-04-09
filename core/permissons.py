from rest_framework import permissions


class IsOwnerOrStaff(permissions.BasePermission):
    message = 'Вы не являетесь владельцем или админом.'

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated or request.user.is_staff:
            return True
        return False
