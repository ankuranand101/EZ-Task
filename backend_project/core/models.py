from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# 1. Custom User with Roles
class User(AbstractUser):
    ROLE_CHOICES = (
        ('OPS', 'Ops User'),
        ('CLIENT', 'Client User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

# 2. Uploaded File Model
class UploadedFile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
