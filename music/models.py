from django.db import models

class Song(models.Model):
    name = models.CharField(max_length=200)
    difficulty = models.IntegerField(default=0)
    artist = models.CharField(max_length=200)

class Comp(models.Model):
    song1 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="matches")
    song2 = models.ForeignKey(Song, on_delete=models.CASCADE)
    similarity = models.FloatField(default=0)