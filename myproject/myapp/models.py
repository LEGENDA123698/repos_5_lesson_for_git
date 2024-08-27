from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
class Game(models.Model):
    title = models.CharField(max_length = 100)
    genre = models.ManyToManyField(Genre, max_length = 100)
    date = models.IntegerField()
    rating = models.IntegerField()


