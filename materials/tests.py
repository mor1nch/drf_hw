from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from materials.models import Course, Lesson
from users.models import User, Subscription


class LessonCourseTests(TestCase):

    def setUp(self):
        self.client = APIClient()

        User.objects.all().delete()

        self.user = User.objects.create(
            email='user@example.com',
            password='password123',
        )
        self.other_user = User.objects.create(
            email='other@example.com',
            password='password456',
        )

        self.course = Course.objects.create(title='Курс 1', description='Описание курса')

        self.lesson = Lesson.objects.create(
            course=self.course,
            title='Урок 1',
            description='Описание урока',
            video_url='https://youtube.com/test'
        )

    def test_create_lesson_authenticated(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('materials:lesson-create')
        data = {
            'course': self.course.id,
            'title': 'Новый урок',
            'description': 'Описание нового урока',
            'video_url': 'https://youtube.com/new'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_lesson_unauthenticated(self):
        url = reverse('materials:lesson-create')
        data = {
            'course': self.course.id,
            'title': 'Новый урок',
            'description': 'Описание нового урока',
            'video_url': 'https://youtube.com/new'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_lesson_list(self):
        url = reverse('materials:lesson-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_retrieve_lesson_detail(self):
        url = reverse('materials:lesson-detail', args=[self.lesson.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.lesson.title)

    def test_update_lesson_authenticated(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('materials:lesson-update', args=[self.lesson.id])
        data = {
            'title': 'Обновленный урок',
            'description': 'Обновленное описание',
            'video_url': self.lesson.video_url,
            'course': self.course.id
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.lesson.refresh_from_db()
        self.assertEqual(self.lesson.title, 'Обновленный урок')

    def test_delete_lesson_authenticated(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('materials:lesson-delete', args=[self.lesson.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Lesson.objects.filter(id=self.lesson.id).exists())

    def test_subscribe_to_course(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('course-subscribe')
        data = {'course_id': self.course.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Subscription.objects.filter(user=self.user, course=self.course).exists())

    def test_unsubscribe_from_course(self):
        Subscription.objects.create(user=self.user, course=self.course)

        self.client.force_authenticate(user=self.user)
        url = reverse('course-subscribe')
        data = {'course_id': self.course.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Subscription.objects.filter(user=self.user, course=self.course).exists())