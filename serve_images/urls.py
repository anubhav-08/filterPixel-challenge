from django.urls import path
from .views import S3ImagesView, GoogleImagesView

urlpatterns = [
    path('', S3ImagesView.as_view()), 
    path('google/', GoogleImagesView.as_view()), 

]