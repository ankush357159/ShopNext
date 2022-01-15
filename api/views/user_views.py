# Django import
from django.contrib.auth.models import User

# Rest Framework jwt
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

# Rest Framework import
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated


# Local Import
from api.serializers import ChangePasswordSerializer, MyTokenObtainPairSerializer, RegisterUserSerializer

# JWT simple token view
class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny,]
    serializer_class = MyTokenObtainPairSerializer    


class LogoutView(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

# Create New User
class RegisterUserCreatView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny,]
    serializer_class = RegisterUserSerializer

# Get User Details
class RegisterUserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = RegisterUserSerializer

# Update User Details PUT & PATCH
class RegisterUserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = RegisterUserSerializer

# Delete User
class RegisterUserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = RegisterUserSerializer

# List All Users
class RegisterUserListView(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = RegisterUserSerializer

# Change Password
class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = ChangePasswordSerializer








