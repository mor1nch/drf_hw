from django.urls import path
from rest_framework.routers import DefaultRouter

from materials import views
from materials.apps import MaterialsConfig

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'course', views.CourseViewSet, basename='course')

urlpatterns = [
    path('lesson/create/', views.LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/', views.LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>/', views.LessonDetailAPIView.as_view(), name='lesson-detail'),
    path('lesson/update/<int:pk>/', views.LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lesson/delete/<int:pk>/', views.LessonDeleteAPIView.as_view(), name='lesson-delete'),
]
urlpatterns += router.urls
