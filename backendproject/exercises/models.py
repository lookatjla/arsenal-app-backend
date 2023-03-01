# Create your models here.
from django.db import models


# Create your models here.
class Exercise(models.Model):
    exercise_name = models.CharField(max_length=50)
    resistance = models.CharField(max_length=50)
    comments = models.CharField(max_length=500)
