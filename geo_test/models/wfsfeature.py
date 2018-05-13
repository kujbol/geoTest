from django.db import models


class WFSFeature(models.Model):
    url = models.URLField()

    name_source = models.CharField(max_length=1024)
    geo_source = models.CharField(max_length=1024)
