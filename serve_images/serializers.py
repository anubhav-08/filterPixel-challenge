from rest_framework import serializers
from .utils import fetch_s3_images

class S3ImagesSerializer(serializers.Serializer):
    image_url = serializers.SerializerMethodField()
    def get_image_url(self, obj):
        return {"images" : fetch_s3_images()}