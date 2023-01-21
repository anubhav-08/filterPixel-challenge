from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import AuthenticationFailed

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password"]
        write_only_fields = ['password']


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)   
    password = serializers.CharField(max_length=68, min_length=5, write_only=True)
    username = serializers.CharField(max_length=68, min_length=5, read_only=True)
    tokens = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ["email", "password", 'username', 'tokens']

    def get_tokens(self, obj):
        user = User.objects.get(username=obj['username'])
        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed("Invalid Credentials")
        
        return {
            'email' : user.email,
            'username' : user.username,
            'tokens' : user.tokens
        }

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ('username', 'password', 'password2',
            'email')
        # extra_kwargs = {
        # 'first_name': {'required': True},
        # 'last_name': {'required': True}
        # }
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs
    def create(self, validated_data):
        user = User.objects.create(
        username=validated_data['username'],
        email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
