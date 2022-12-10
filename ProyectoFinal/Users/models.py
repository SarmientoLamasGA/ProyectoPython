from django.db import models
from django.conf import settings

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    email = models.EmailField(max_length=50, null=False)
    name = models.CharField(max_length=40, null=False)
    lastName = models.CharField(max_length=40, null=False)
    author = models.BooleanField(null=False)