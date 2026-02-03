from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('staff', 'Staff (Class/Year Coordinator)'),
        ('admin', 'Admin (HOD)'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    register_no = models.CharField(max_length=20, blank=True, null=True)  # For students
    staff_id = models.CharField(max_length=20, blank=True, null=True)  # For staff/admin
    program = models.CharField(max_length=100, blank=True, null=True)
    section = models.CharField(max_length=10, blank=True, null=True)
