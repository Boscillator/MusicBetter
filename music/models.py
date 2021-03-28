from django.db import models

class Song(models.Model):
    name = models.CharField(max_length=200)
    difficulty = models.IntegerField(default=0)
    artist = models.CharField(max_length=200)

class Comp(models.Model):
    song1 = models.CharField(max_length=200) 
    song2 = models.CharField(max_length=200)
    similarity = models.FloatField(default=0)