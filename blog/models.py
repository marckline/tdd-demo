from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey("Author")

class Author(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=64, blank=True)