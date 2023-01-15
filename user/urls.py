from django.urls import path
from .views import UserView


# from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('', UserView.as_view(), name="register"),
]