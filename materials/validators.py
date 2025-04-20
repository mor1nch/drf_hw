from urllib.parse import urlparse

from rest_framework.exceptions import ValidationError


def validate_youtube_url(value):
    parsed_url = urlparse(value)
    link = parsed_url.netloc.lower()

    if not 'youtube.com' in link:
        raise ValidationError("Ссылка должна быть на youtube.com")
    return value
