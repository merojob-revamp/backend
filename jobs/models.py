from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    required_experience = models.IntegerField()
    duration = models.IntegerField()

    def __str__(self):
        return self.title