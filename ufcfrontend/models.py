from django.db import models

# Create your models here.
class Fighter(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    currentDivision = models.CharField(max_length=100)
    record = models.CharField(max_length=100)
    img = models.CharField(max_length=200)
    age = models.IntegerField()
