# Create your models here.
from django.db import models
from datetime import datetime

class Bin(models.Model):
    location = models.CharField(max_length=100)
    capacity = models.IntegerField()
    current_level = models.IntegerField()
    last_collected = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.location

