from rest_framework.viewsets import ModelViewSet

from core.api.serializers import UserSerializer, CommentSerializer, PostSerializer
from core.models import User, Post, Comment
from core.permissons import UserPermission, PostPermission, CommentPermission


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserPermission,)




class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (PostPermission,)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (CommentPermission,)

