from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Deal(models.Model):
    name = models.TextField(max_length=200)
    image = models.URLField()
    rating = models.FloatField()
    link = models.URLField()
    actual_price = models.FloatField()
    discount = models.FloatField()
    location = models.TextField()
    