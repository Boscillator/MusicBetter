from django.db import models

class Song(models.Model):
    id = models.CharField(max_length=20, unique=True, primary_key=True)
    name = models.TextField()
    artist = models.TextField(null=True)
    album = models.TextField(null=True)
    genera = models.TextField(null=True)
    style = models.TextField(null=True)
    year = models.IntegerField(null=True)
    difficulty = models.IntegerField(null=True)

class Comp(models.Model):
    song1 = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="matches")
    song2 = models.ForeignKey(Song, on_delete=models.CASCADE)
    similarity = models.FloatField(default=0)