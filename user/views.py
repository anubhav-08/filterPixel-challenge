from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,RegisterSerializer, LoginSerializer
from django.contrib.auth import get_user_model
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics, status

User = get_user_model()

# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    def get(self,request,*args,**kwargs):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

# Login based view to login user along with generation of auth token
# class LoginUserAPIView(generics.GenericAPIView):
#     permission_classes = (AllowAny,)
#     serializer_class = LoginSerializer

#     def post(self, request):
#         data = {}
#         req_body = request.data
#         email = req_body['email']
#         password = req_body['password']
#         try:

#             Account = User.objects.get(email = email)
#         except BaseException as e:
#             raise ValidationError({"400": f'{str(e)}'})

#         token = Token.objects.get_or_create(user=Account)[0].key
#         print(token)
#         if not Account.check_password(password):
#             raise ValidationError({"message": "Incorrect Login credentials"})

#         if Account:
#             if Account.is_active:
#                 print(request.user)
#                 login(request, Account)
#                 data["message"] = "user logged in"
#                 data["email_address"] = Account.email

#                 Res = {"data": data, "token": token}

#                 return Response(Res)

#             else:
#                 raise ValidationError({"400": f'Account not active'})

#         else:
#             raise ValidationError({"400": f'Account doesnt exist'})


class LoginUserAPIView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    def post(self, request):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
