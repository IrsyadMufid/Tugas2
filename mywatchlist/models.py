from django.db import models


class MyWatchlist(models.Model):
    watched = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    rating = models.FloatField()
    release_date = models.TextField()
    review = models.TextField()
