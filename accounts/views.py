# accounts/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from .serializers import RegistrationSerializer, LoginSerializer, TokenRefreshSerializer, UserSerializer, JobSeekerSerializer
from .models import JobSeeker
from rest_framework.permissions import IsAuthenticated

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
        
        return Response({
            "access_token": str(RefreshToken.for_user(user)),
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "has_filled_profile": user.has_filled_profile
        })

class TokenRefreshView(TokenRefreshView):
    serializer_class = TokenRefreshSerializer


class JobSeekerUpdateView(generics.UpdateAPIView):
    queryset = JobSeeker.objects.all()
    serializer_class = JobSeekerSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.jobseeker

# class CompanyUpdateView(generics.UpdateAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer
#     permission_classes = [IsAuthenticated]

#     def get_object(self):
#         return self.request.user.company