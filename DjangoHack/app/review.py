from django.db import models

class review_source(models.Model):
    name = models.CharField()
    url = models.URLField()

class review(models.Model):
    text = models.CharField()
    source = models.ForeignKey(review_source, on_delete=models.CASCADE)
    url = models.URLField()
    sence = models.FloatField()




