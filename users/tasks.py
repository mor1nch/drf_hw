from datetime import timedelta

from celery import shared_task
from celery.utils.time import timezone

from users.models import User


@shared_task
def block_inactive_users() -> int:
    month_ago = timezone.now() - timedelta(days=30)

    users = User.objects.filter(is_active=True, is_superuser=False, last_login__lte=month_ago)
    users.update(is_active=False)

    return users.count()
