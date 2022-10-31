from django.db import models
# Create your models here.

class Thing(models.Models):
    name = models.CharField()
    description = models.CharField()
    quantity = models.IntegerField()