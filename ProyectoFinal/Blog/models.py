from django.db import models

class Post(models.Model):

    title = models.CharField(max_length = 100)
    date = models.DateTimeField()
    body = models.TextField()
    tags = models.CharField(max_length = 100)
    author = models.CharField(max_length = 50)
    image = models.ImageField(upload_to="images", null=True, blank=True)

class Comments(models.Model):

    user = models.CharField(max_length = 50)
    body_comment = models.TextField()
    post_id = models.IntegerField(null=True)