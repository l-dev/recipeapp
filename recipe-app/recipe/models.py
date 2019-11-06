from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    photo_url = models.TextField()
    def __str__(self):
        return self.name
class Comments(models.Model):
    body = models.CharField(max_length=100)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    def __str__(self):
        return self.body
# Create your models here.
