from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet

from core.api.serializers import UserSerializer, CommentSerializer, PostSerializer
from core.models import User, Post, Comment
from core.permissons import IsOwnerOrStaff
from rest_framework.permissions import AllowAny, IsAuthenticated


class UserViewSet(ModelViewSet):
    """Viewset для работы с данными пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    authentication_classes = (TokenAuthentication,)

    def get_permissions(self):
        """
            Разрешения для Api пользователя со следующими критериями:**
            - create: все пользователи (регистрация)
            - read: администратор/авторизованные пользователи
            - update: администратор/пользователь может редактировать только себя
            - delete: администратор
            """
        permission_classes = (AllowAny,)
        if self.action in ["create"]:
            permission_classes = (AllowAny,)
        if self.action in ["retrieve"]:
            permission_classes = (IsAuthenticated,)
        elif self.action in ["update", "partial_update", "destroy"]:
            permission_classes = (IsOwnerOrStaff,)
        return tuple(permission() for permission in permission_classes)


class PostViewSet(ModelViewSet):
    """Viewset для работы с данными постов"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
    authentication_classes = (TokenAuthentication,)

    def get_permissions(self):
        """
            **Разрешения для Api поста со следующими критериями:**
            - create: авторизованные пользователи
            - read: все пользователи
            - update: администратор/пользователь может редактировать только себя
            - delete: администратор/пользователь может удалять свои посты
            """
        permission_classes = (AllowAny,)
        if self.action in ["retrieve"]:
            permission_classes = (AllowAny,)
        if self.action in ["create"]:
            permission_classes = (IsAuthenticated,)
        elif self.action in ["update", "partial_update", "destroy"]:
            permission_classes = (IsOwnerOrStaff,)
        return tuple(permission() for permission in permission_classes)


class CommentViewSet(ModelViewSet):
    """Viewset для работы с данными комментариев"""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]
    authentication_classes = (TokenAuthentication,)

    def get_permissions(self):
        """
            **Разрешения для Api комментариев со следующими критериями:**
            - create: авторизованные пользователи
            - read: все пользователи
            - update: администратор/пользователь может редактировать только себя
            - delete: администратор/пользователь может удалять свои комментарии
            """
        permission_classes = (AllowAny,)
        if self.action in ["retrieve"]:
            permission_classes = (AllowAny,)
        if self.action in ["create"]:
            permission_classes = (IsAuthenticated,)
        elif self.action in ["update", "partial_update", "destroy"]:
            permission_classes = (IsOwnerOrStaff,)
        return tuple(permission() for permission in permission_classes)
