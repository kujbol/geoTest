from django.views.generic import ListView

from geo_test.models import Quiz


class ChooseQuiz(ListView):
    template_name = 'choose_quiz.html'
    queryset = Quiz.objects.all().order_by('id')
    paginate_by = 10

