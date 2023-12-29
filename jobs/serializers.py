from .models import Job
from rest_framework import serializers
from accounts.serializers import UserSerializer


class JobSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Job
        fields = '__all__'
        read_only_fields = ('job_id', 'created_by', 'created_at')