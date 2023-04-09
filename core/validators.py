from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator


# user validators
def validate_password(password: str):
    """ Валидатор пароля проверяющий содержит ли пароль хоть одну цифру и соответствует длине больше 8 символов"""
    if len(password) < 8:
        raise ValidationError('Пароль должен быть длинее 8 символов')
    if (any(char.isdigit() for char in password)) is False:
        raise ValidationError('Пароль должен содержать цифры')


def correct_email_validator(email):
    """ Корректно работающий валидатор почты на базе встроенного валидатора"""
    try:
        EmailValidator(email)
    except:
        raise ValidationError('Введите правильный адрес почты')

    allow_list = ["mail.ru", "yandex.ru"]
    if email.split('@')[-1] not in allow_list:
        raise ValidationError('Регистрация разрешена только с доменов mail.ru и yandex.ru.')


# Post validators
def censored_title(title):
    """ Валидатор заголовка проверяющий не содержит ли заголовок нецензурных слов находящихся в запрещенном списке"""
    obscene_language = ["ерунда", "глупость", "чепуха"]
    if title.lower() in obscene_language:
        raise ValidationError("В заголовок нельзя включать нецензурные слова")
