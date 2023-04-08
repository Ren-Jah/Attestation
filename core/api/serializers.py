from rest_framework import serializers
from core.models import User, Post, Comment


# User serializers
# class UserCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = [
#             "id",
#             "username",
#             "password",
#             "birth_date",
#         ]
#
#     def create(self, validated_data):
#         user = super().create(validated_data)
#         user.set_password(user.password)
#         user.save()
#         return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "birth_date",
            "email",

        ]

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(user.password)
        user.save()
        return user


# Post serializers
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "text",
            "author",
            "comments",

        ]


# Comment serializers
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "id",
            "text",
            "author",
        ]
