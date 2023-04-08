from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import EmailValidator

from datetime import date
from dateutil.relativedelta import relativedelta
from django.core.exceptions import ValidationError

from core.validators import validate_password, censored_title


class DatesModelMixin(models.Model):
    """`DatesModelMixin` add `created` and `updated` fields. These fields will update automatically on `save()`."""

    class Meta:
        abstract = True

    created = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateField(auto_now=True, verbose_name="Дата последнего обновления")


class UserRole:
    MEMBER = 'member'
    ADMIN = 'admin'
    choices = ((MEMBER, 'Пользователь'),
               (ADMIN, 'Администратор'))


class User(AbstractUser, DatesModelMixin):

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    username = models.CharField(unique=True, verbose_name="Логин", max_length=255)
    password = models.CharField(verbose_name="Пароль", max_length=255, validators=[validate_password])
    phone_num = models.CharField(verbose_name="Телефонный номер", max_length=30, blank=True, null=True)
    birth_date = models.DateField(verbose_name="Дата рождения", blank=True, null=True)
    role = models.CharField(verbose_name="Роль", choices=UserRole.choices, default=UserRole.MEMBER, max_length=20)
    email = models.EmailField(verbose_name="эл.почта", blank=True,  validators=[EmailValidator(
        message="Регистрация с данного домена запрещена.",
        allowlist=["mail.ru", "yandex.ru"])])

    def __str__(self):
        return f'{self.username}'


# post validators
def check_birth_date(obj):
    birth_date = User.objects.get_by_natural_key(obj).birth_date
    diff = relativedelta(date.today(), birth_date).years
    if diff < 18:
        raise ValidationError("Автор поста не достиг 18 лет")


class Comment(DatesModelMixin):

    class Meta:
        verbose_name = "Коммент"
        verbose_name_plural = "Комменты"

    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.RESTRICT)
    text = models.TextField(verbose_name="Текст", max_length=255)

    def __str__(self):
        return f'{self.text}'


class Post(DatesModelMixin):

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    title = models.CharField(verbose_name="Заголовок", max_length=255, validators=[censored_title])
    text = models.TextField(verbose_name="Текст", max_length=255)
    image = models.ImageField(verbose_name="Изображение", upload_to='post_images', null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.RESTRICT, validators=[check_birth_date])
    comments = models.ManyToManyField(Comment, verbose_name="Комментарии", blank=True)

    def __str__(self):
        return f'{self.title} {self.text} '









