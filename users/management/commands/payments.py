from django.core.management import BaseCommand

from materials.models import Course, Lesson
from users.models import Payments, User


class Command(BaseCommand):
    help = 'Создание платежей'

    def handle(self, *args, **kwargs):
        User.objects.all().delete()
        Payments.objects.all().delete()

        user = User.objects.create(
            email='email@example.com',
            first_name='Denis',
            last_name='Stepanov',
            is_staff=True,
            is_superuser=True,
        )
        user.set_password("password")
        user.save()

        Payments.objects.create(
            user=user,
            course_id=1,
            lesson_id=1,
            amount=10,
            payment_type="Cash",
        )

        Payments.objects.create(
            user=user,
            course_id=1,
            lesson_id=2,
            amount=12,
            payment_type="Debit card",
        )
