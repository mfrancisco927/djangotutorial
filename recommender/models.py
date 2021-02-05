from django.db import models

class Musicdata(models.Model):
    id = models.TextField(primary_key=True)
    valence = models.FloatField()
    year = models.IntegerField()
    acousticness = models.FloatField()
    danceability = models.FloatField()
    energy = models.FloatField()
    popularity = models.FloatField()
    artists = models.TextField()
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'musicdata'
