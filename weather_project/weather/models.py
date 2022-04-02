
from django.db import models


class City(models.Model):
    name = models.CharField(max_length=25)
    icon = models.CharField(max_length=200)
    temperature = models.FloatField()
    description = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name
