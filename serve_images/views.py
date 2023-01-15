from rest_framework.response import Response
from rest_framework import generics
from .serializers import S3ImagesSerializer
from .utils import fetch_s3_images, fetch_google_images

class S3ImagesView(generics.GenericAPIView):
    def get(self, request):
        img_urls = fetch_s3_images()
        return Response({'data' : img_urls})

class GoogleImagesView(generics.GenericAPIView):
    def get(self, request):
        img_urls = fetch_google_images()
        return Response({'data' : img_urls})