from urllib.parse import urlparse

from rest_framework.serializers import ValidationError


def validate_link(value):
    """Проверка на отсутствие в материалах ссылок на сторонние ресурсы, кроме youtube.com"""

    if value:
        parsed_url = urlparse(value)
        if "youtube.com" not in parsed_url.netloc:
            raise ValidationError("Можно добавлять только ссылки на YouTube.")
