from rest_framework.response import Response
from rest_framework import generics
from .serializers import S3ImagesSerializer
from .utils import fetch_s3_images, fetch_google_images
import json

class S3ImagesView(generics.GenericAPIView):
    def get(self, request):
        img_urls = json.dumps({
                    'data' :   fetch_s3_images()
        })

        return Response(img_urls)

class GoogleImagesView(generics.GenericAPIView):
    def get(self, request):
        img_urls = json.dumps({
                    'data' : fetch_google_images()
        })
        return Response(img_urls)