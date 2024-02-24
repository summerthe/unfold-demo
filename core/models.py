from django.db import models

class Driver(models.Model):
    title = models.CharField(max_length=255)