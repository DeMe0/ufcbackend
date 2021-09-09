from django.db import models

# Create your models here.
class Fighter(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    currentDivision = models.CharField(max_length=100)
    record = models.CharField(max_length=100)
    img = models.CharField(max_length=200)
