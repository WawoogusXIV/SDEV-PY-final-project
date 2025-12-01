from django.db import models

# Create your models here.
from django.conf import settings
from django.utils import timezone

class Showings(models.Model):
    title = models.CharField(max_length=100)


    def __str__(self):
        return self.title