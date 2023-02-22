from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length = 50)
    country = models.CharField(max_length = 30)
    birth_year = models.IntegerField()
    genre = models.CharField(max_length = 150)
    
class Song(models.Model):
   Title = models.CharField(max_length = 50)
   release_date = models.IntegerField()
   length = models.DateField()
   artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
   