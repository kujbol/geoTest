from django.views.generic import ListView

from geo_test.models import QuizResult


class LeaderBoard(ListView):
    model = QuizResult
    paginate_by = 10

    template_name = 'leader_board.html'

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.kwargs.get('quiz_id'):
            queryset = queryset.filter(quiz=self.kwargs.get('quiz_id'))

        return queryset.order_by('-score')
