from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group, Permission


class JobSeeker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100,null=True, blank=True)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100,null=True , blank=True)
    phone_number = models.CharField(max_length=20,null=True, blank=True)
    address = models.CharField(max_length=100,null=True, blank=True)
    permanent_address = models.CharField(max_length=100,null=True , blank=True)
    current_address = models.CharField(max_length=100,null=True, blank=True)
    level_of_education = models.CharField(max_length=100,null=True, blank=True)
    faculty = models.CharField(max_length=100,null=True, blank=True)
    graduation_year = models.IntegerField(null=True, blank=True)
    gpa = models.FloatField(null=True, blank=True)
    previous_company = models.CharField(max_length=100, null=True, blank=True)
    previous_role = models.CharField(max_length=100, null=True, blank=True)
    interested_category = models.CharField(max_length=100, null=True, blank=True)
    interested_role = models.CharField(max_length=100, null=True, blank=True)
    interested_employment_type = models.CharField(max_length=100, null=True, blank=True)
    expected_position_level = models.CharField(max_length=100, null=True, blank=True)
    upload_resume = models.FileField(upload_to='resumes/', null=True, blank=True)

    def __str__(self):
        return self.user.username
    
    def is_filled(self):
        fields = [
            'first_name', 'middle_name', 'last_name', 'phone_number', 'address', 'permanent_address', 'current_address',
            'level_of_education', 'faculty', 'graduation_year', 'gpa', 'previous_company', 'previous_role',
            'interested_category', 'interested_role', 'interested_employment_type', 'expected_position_level',
            'upload_resume'
        ]
        for field in fields:
            if not getattr(self, field):
                return False
        return True