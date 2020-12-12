"""
Definition of models.
"""
from django.db import models

class review_source(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()

class review(models.Model):
    text = models.CharField(max_length=20000)
    source = models.ForeignKey(review_source, on_delete=models.CASCADE)
    url = models.URLField()
    sence = models.FloatField()