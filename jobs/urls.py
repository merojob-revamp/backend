from django.urls import path
from .views import JobCreateView, JobListView

urlpatterns = [
    path('create/', JobCreateView.as_view(), name='job-create'),
    path('list/', JobListView.as_view(), name='job-list'),
]