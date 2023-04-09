from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.contrib.auth.models import Group

from core.models import User, Comment, Post


class UserAdmin(admin.ModelAdmin):
    list_display = ("username",  "phone_num", "birth_date", "is_staff", "email")
    list_filter = ("username", "birth_date")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("author_link", "text")
    list_filter = ("author", "text")

    def author_link(self, obj):
        """Функция позволяющая перенаправить на страницу редактирования автора поста"""
        url = reverse("admin:core_user_change", args=[obj.author.id])
        return format_html(f'<a href="{url}">{obj.author}</a>')


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "text", "author_link")
    list_filter = ("title",)

    def author_link(self, obj):
        """Функция позволяющая перенаправить на страницу редактирования автора поста"""
        url = reverse("admin:core_user_change", args=[obj.author.id])
        return format_html(f'<a href="{url}">{obj.author}</a>')


admin.site.register(User, UserAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)

admin.site.unregister(Group)
