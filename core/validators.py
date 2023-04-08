from django.core.exceptions import ValidationError


# user validators
def validate_password(password: str):
    if len(password) < 8:
        raise ValidationError('Пароль должен быть длинее 8 символов')
    if (any(char.isdigit() for char in password)) is False:
        raise ValidationError('Пароль должен содержать цифры')


def censored_title(title):
    obscene_language = ["ерунда", "глупость", "чепуха"]
    if title.lower() in obscene_language:
        raise ValidationError("В заголовок нельзя включать нецензурные слова")
