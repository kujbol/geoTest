from django.contrib.gis.db import models

from geo_test.models.quiz import Quiz


class Question(models.Model):
    geo = models.GeometryField()

    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)
    quiz = models.ForeignKey(
        Quiz, related_name='questions', on_delete=models.CASCADE
    )
