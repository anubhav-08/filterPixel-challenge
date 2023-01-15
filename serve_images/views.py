from rest_framework.response import Response
from rest_framework import generics
from .serializers import S3ImagesSerializer
from .utils import fetch_s3_images

class S3ImagesView(generics.GenericAPIView):
    def get(self, request):
        data = fetch_s3_images()
        print(data)
        return Response({'data' : data})

class GoogleImagesView(generics.GenericAPIView):
    def get(self, request):
        data = fetch_s3_images()
        print(data)
        return Response({'data' : data})