from django.urls import path

from users import views

urlpatterns = [
    path('payments/', views.PaymentsListAPIView.as_view(), name='payments'),
]
