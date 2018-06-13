from django.contrib.auth.models import User
from django.db import models

from geo_test.models.wfsfeature import WFSFeature


class Quiz(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()

    data_source = models.OneToOneField(WFSFeature, on_delete=models.CASCADE)

    question_number = models.IntegerField(
        default=20, help_text='Number of questions which are served to user'
    )

    @property
    def questions_to_answer(self):
        return min(self.questions.count(), self.question_number)


class QuizResult(models.Model):
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name='quiz_results'
    )
    score = models.IntegerField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_quiz_results'
    )
