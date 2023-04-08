from rest_framework.permissions import BasePermission, IsAuthenticated, IsAdminUser


# User permissions
class UserPermission(BasePermission):
    """**Пользователь:**
    - create: все пользователи (регистрация)
    - read: администратор/авторизованные пользователи
    - update: администратор/пользователь может редактировать только себя
    - delete: администратор
    """
    def has_permission(self, request, view):
        if view.action == 'list':
            return request.user.is_authenticated or request.user.is_staff
        elif view.action == 'create':
            return True
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        # Deny actions on objects if the user is not authenticated
        if not request.user.is_authenticated:
            return False

        if view.action == 'retrieve':
            return obj == request.user or request.user.is_staff
        elif view.action in ['update', 'partial_update']:
            return obj == request.user or request.user.is_staff
        elif view.action == 'destroy':
            return request.user.is_staff
        else:
            return False



# Post permissions
class PostPermission(BasePermission):
    """
    **Пост:**
    - create: авторизованные пользователи
    - read: все пользователи
    - update: администратор/пользователь может редактировать только себя
    - delete: администратор/пользователь может удалять свои посты
    """
    def has_permission(self, request, view):
        if view.action == 'create':
            return request.user.is_authenticated or request.user.is_staff
        elif view.action == 'list':
            return True
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        # Deny actions on objects if the user is not authenticated
        if not request.user.is_authenticated:
            return False
        if view.action == 'retrieve':
            return obj == request.user or request.user.is_staff
        elif view.action in ['update', 'partial_update']:
            return obj == request.user or request.user.is_staff
        elif view.action == 'destroy':
            return request.user.is_staff
        else:
            return False


# Comment permissions
class CommentPermission(BasePermission):
    """
    **Комментарий:**
    - create: авторизованные пользователи
    - read: все пользователи
    - update: администратор/пользователь может редактировать только себя
    - delete: администратор/пользователь может удалять свои комментарии
    """
    def has_permission(self, request, view):
        if view.action == 'create':
            return request.user.is_authenticated or request.user.is_staff
        elif view.action == 'list':
            return True
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        # Deny actions on objects if the user is not authenticated
        if not request.user.is_authenticated:
            return False

        if view.action == 'retrieve':
            return obj == request.user or request.user.is_staff
        elif view.action in ['update', 'partial_update']:
            return obj == request.user or request.user.is_staff
        elif view.action == 'destroy':
            return request.user.is_staff
        else:
            return False
