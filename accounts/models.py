from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group, Permission

# Create your models here.

'''
There will be two types of account. One for the normal jobseeking user and another for the companies.

The jobseeking user will have the following fields:
Personal Information:
- username
- password
- email
- first name
- middle name
- last name
- phone number
- address
- Permanent Address
- Current Address

Educational Information:
- Level of Education
- Faculty
- Graduation Year
- Another Level of Education
- Another Faculty
- Another Graduation Year
- GPA/Percentage

Work Experience:
- Previous Company
- Previous Role
- Interested Category
- Interested Role
- Interested Employment Type
- Expected Position Level
- Upload Resume

The company user will have the following fields:
Company Information:
- username
- password
- email
- company name
- company website
- company phone number
- company address
- company description
- company logo
- company size
- company type
- company industry

'''

class BasicUser(User):
    has_filled_profile = models.BooleanField(default=False)

class JobSeeker(models.Model):
    user = models.OneToOneField(BasicUser, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    permanent_address = models.CharField(max_length=100)
    current_address = models.CharField(max_length=100)
    level_of_education = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    graduation_year = models.IntegerField()
    another_level_of_education = models.CharField(max_length=100, null=True, blank=True)
    another_faculty = models.CharField(max_length=100, null=True, blank=True)
    another_graduation_year = models.IntegerField(null=True, blank=True)
    gpa = models.FloatField()
    previous_company = models.CharField(max_length=100, null=True, blank=True)
    previous_role = models.CharField(max_length=100, null=True, blank=True)
    interested_category = models.CharField(max_length=100, null=True, blank=True)
    interested_role = models.CharField(max_length=100, null=True, blank=True)
    interested_employment_type = models.CharField(max_length=100, null=True, blank=True)
    expected_position_level = models.CharField(max_length=100, null=True, blank=True)
    upload_resume = models.FileField(upload_to='resumes/', null=True, blank=True)

    def __str__(self):
        return self.user.username


# class Company(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     company_name = models.CharField(max_length=100)
#     company_website = models.CharField(max_length=100)
#     company_phone_number = models.CharField(max_length=20)
#     company_address = models.CharField(max_length=100)
#     company_description = models.CharField(max_length=100)
#     company_logo = models.ImageField(upload_to='logos/')
#     company_size = models.CharField(max_length=100)
#     company_type = models.CharField(max_length=100)
#     company_industry = models.CharField(max_length=100)

#     def __str__(self):
#         return self.user.username
