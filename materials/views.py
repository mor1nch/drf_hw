from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from materials.models import Course, Lesson
from materials.paginators import MaterialsPagination
from materials.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления курсами (Course).
    Поддерживает полный CRUD:
    - GET /course/ — список курсов
    - POST /course/ — создание нового курса
    - GET /course/{id}/ — получение конкретного курса
    - PUT/PATCH /course/{id}/ — обновление курса
    - DELETE /course/{id}/ — удаление курса

    Используется пагинация MaterialsPagination.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = MaterialsPagination


class LessonCreateAPIView(generics.CreateAPIView):
    """
    Эндпоинт для создания нового урока (Lesson).
    - POST /lesson/create/

    Требуется аутентификация.
    """
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]


class LessonListAPIView(generics.ListAPIView):
    """
    Эндпоинт для получения списка всех уроков (Lesson).
    - GET /lesson/

    Используется пагинация MaterialsPagination.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = MaterialsPagination


class LessonDetailAPIView(generics.RetrieveAPIView):
    """
    Эндпоинт для получения информации о конкретном уроке.
    - GET /lesson/{id}/
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonUpdateAPIView(generics.UpdateAPIView):
    """
    Эндпоинт для обновления информации об уроке.
    - PUT/PATCH /lesson/{id}/
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDeleteAPIView(generics.DestroyAPIView):
    """
    Эндпоинт для удаления урока.
    - DELETE /lesson/{id}/
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
