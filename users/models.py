from django.contrib.auth.models import AbstractUser
from django.db import models

from config import settings
from materials.models import Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="email")
    phone = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Payments(models.Model):
    PAYMENT_TYPE = [
        ('Cash', 'Наличная'),
        ('Debit card', 'Картой'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    payment_date = models.DateField(auto_now_add=True)
    amount = models.PositiveIntegerField()
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPE)
    session_id = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.user.email} course: {self.course.title}, lesson: {self.lesson.title}"


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscriptions')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='subscriptions')

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"{self.user.email} подписан на {self.course.title}"
