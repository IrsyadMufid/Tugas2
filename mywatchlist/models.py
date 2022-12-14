from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
from datetime import datetime


class MyWatchlist(models.Model):
    watched = models.BooleanField(default=False)
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    release_date = models.DateField(null=True, blank=True)
    review = models.TextField()


