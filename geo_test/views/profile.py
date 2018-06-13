from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Max
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView


@method_decorator(login_required, 'get')
class Profile(UpdateView):
    model = User
    fields = ["username", "email"]
    # the combined UserProfile and User exposes.
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_quiz_results = context['user'].user_quiz_results
        context['high_scores'] = user_quiz_results\
            .values('quiz', 'quiz__name')\
            .annotate(max_score=Max('score'))
        return context
