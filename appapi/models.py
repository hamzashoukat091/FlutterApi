from django.db import models

# Create your models here.
class MovieUpload(models.Model):
    movie_name = models.CharField(max_length=100)
    movie_url = models.FileField(upload_to='movies')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.movie_name)

class Replies(models.Model):
    reply = models.CharField(max_length=1000)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.reply)

class Block(models.Model):
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.reply)