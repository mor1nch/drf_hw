from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users import views
from users.views import SubscriptionCreateAPIView

urlpatterns = [
    path('payments/', views.PaymentsListAPIView.as_view(), name='payments'),
    path('subscribe/', SubscriptionCreateAPIView.as_view(), name='course-subscribe'),
    path('api/token/', TokenObtainPairView.as_view(), name='create_token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
]
