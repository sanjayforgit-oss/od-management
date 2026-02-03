from django.db import models
from accounts.models import User

class ODRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    APPROVAL_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='od_requests')
    register_no = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    section = models.CharField(max_length=10)
    reason = models.TextField()
    from_date = models.DateField()
    to_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    class_coord_approval = models.CharField(max_length=10, choices=APPROVAL_CHOICES, default='pending')
    year_coord_approval = models.CharField(max_length=10, choices=APPROVAL_CHOICES, default='pending')
    hod_approval = models.CharField(max_length=10, choices=APPROVAL_CHOICES, default='pending')
    final_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.register_no} - {self.reason}"
