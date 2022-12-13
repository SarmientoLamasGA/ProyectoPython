from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(User):
    name = models.CharField(max_length=40, null=True)
    lastName = models.CharField(max_length=40, null=True)
    author = models.BooleanField(null=False, default=False)
    def str(self):
        return self.user.username

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="avatares", null=True, blank=True, default="/avatares/BlankProfile.webp")
