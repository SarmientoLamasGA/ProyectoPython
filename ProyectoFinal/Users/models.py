from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20, unique=True, null=False)
    email = models.EmailField(max_length=50, null=False)
    password = models.CharField(max_length=20, null=False)
    name = models.CharField(max_length=40, null=False)
    lastName = models.CharField(max_length=40, null=False)
    writer = models.BooleanField(null=False)