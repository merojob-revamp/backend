# accounts/views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from .serializers import RegistrationSerializer, LoginSerializer, TokenRefreshSerializer, UserSerializer, JobSeekerSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import JobSeeker


class JobSeekerView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JobSeekerSerializer

    def get_object(self):
        return self.request.user.jobseeker

    def put(self, request, *args, **kwargs):
        jobseeker = self.get_object()
        serializer = self.get_serializer(jobseeker, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request, pk=None):
        if pk:
            jobseeker = get_object_or_404(JobSeeker, pk=pk)
            serializer = JobSeekerSerializer(jobseeker)
        else:
            jobseeker = self.get_object()
            serializer = self.get_serializer(jobseeker)
        return Response(serializer.data)

class RegistrationView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

class LoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)

        return Response({
            "access_token": str(refresh.access_token),
            "refresh": str(refresh),
            "user": UserSerializer(user, context=self.get_serializer_context()).data
        })

class TokenRefreshView(TokenRefreshView):
    serializer_class = TokenRefreshSerializer