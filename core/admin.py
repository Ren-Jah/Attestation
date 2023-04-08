from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.contrib.auth.models import Group

from core.models import User, Comment, Post


# @admin.action(description='Обнуляет количество книг')
# def set_quantity_in_zero(modeladmin, request, queryset):
#     queryset.update(quantity_in=0)


class UserAdmin(admin.ModelAdmin):
    list_display = ("username",  "phone_num", "birth_date", "role", "email")
    list_filter = ("username", "birth_date")
    # actions = [set_quantity_in_zero]


class CommentAdmin(admin.ModelAdmin):
    list_display = ("author_link", "text")
    list_filter = ("author", "text")

    def author_link(self, obj):
        url = reverse("admin:core_user_change", args=[obj.author.id])
        return format_html(f'<a href="{url}">{obj.author}</a>')


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "text", "author_link")
    list_filter = ("title",)

    def author_link(self, obj):
        url = reverse("admin:core_user_change", args=[obj.author.id])
        return format_html(f'<a href="{url}">{obj.author}</a>')


admin.site.register(User, UserAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)

admin.site.unregister(Group)
