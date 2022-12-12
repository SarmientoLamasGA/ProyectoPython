from django.db import models

class Post(models.Model):

    title = models.CharField(max_length = 100)
    date = models.DateTimeField()
    body = models.TextField()
    tags = models.CharField(max_length = 100)
    author = models.CharField(max_length = 50)
    image = models.ImageField(upload_to="images_post", null=True, blank=True)

    def __str__(self):
        return f'Autor: {self.author}, Título: {self.title}, Etiquetas: {self.tags}'

class Comments(models.Model):

    user = models.CharField(max_length = 50)
    body_comment = models.TextField()
    post_id = models.IntegerField(null=True)

    def __str__(self):
        return f'Comentario del usuario: {self.user}'