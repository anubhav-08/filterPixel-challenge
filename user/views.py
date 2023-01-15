from django.contrib.auth.models import User
from user.serializers import UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

class UserView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def get(self, request):
        
        print(request)
        users = User.objects.first()
        data = UserSerializer(users)
        # data.is_valid(raise_exception=True)
        print(data)
        return Response({"message" : "logged in"})
    
    # def post()