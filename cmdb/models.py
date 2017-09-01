from django.db import models

# Create your models here.
class liuyan(models.Model):
    name = models.CharField(max_length=128)
    dateTime=models.CharField(max_length=128)
    content=models.CharField(max_length=2000)