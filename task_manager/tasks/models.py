from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('LOW', 'LOW'),
        ('MEDIUM', 'MEDIUM'),
        ('HIGH', 'HIGH'),
    ]

    STATUS_CHOICES = [
        ('PENDING', 'PENDING'),
        ('COMPLETED', 'COMPLETED'),
    ]

    Title = models.CharField(max_length=100)
    
    Description = models.TextField(blank = True)
    
    Due_Date = models.DateField()
    
    Priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES)
    
    Status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    
    User = models.ForeignKey(User, on_delete=models.CASCADE, realted_name='tasks')
    
    Completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.Title