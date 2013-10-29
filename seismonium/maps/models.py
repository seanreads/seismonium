from django.db import models

# Create your models here.

class Setting(models.Model):
  name = models.CharField(max_length=25)
  value = models.CharField(max_length=255)

class Earthquake(models.Model):
  geojson = models.TextField()
  cached_at = models.DateTimeField(auto_now=True)
