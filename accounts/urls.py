from django.urls import path
from .views import RegistrationView, LoginView, TokenRefreshView, JobSeekerUpdateView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jobseeker/update/', JobSeekerUpdateView.as_view(), name='jobseeker_update'),
]