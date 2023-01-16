from django.urls import path
from .views import UserDetailAPI,RegisterUserAPIView, LoginUserAPIView


urlpatterns = [
  path("get-details",UserDetailAPI.as_view()),
  path('register',RegisterUserAPIView.as_view()),
  path('login/', LoginUserAPIView.as_view()),
]