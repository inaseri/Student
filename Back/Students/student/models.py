from django.db import models


class Students(models.Model):
    name = models.CharField(max_length=400)
    age = models.IntegerField()
    address = models.CharField(max_length=800)
