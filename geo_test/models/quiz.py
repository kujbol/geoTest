from django.db import models

from geo_test.models.wfsfeature import WFSFeature


class Quiz(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()

    data_source = models.OneToOneField(WFSFeature, on_delete=models.CASCADE)
