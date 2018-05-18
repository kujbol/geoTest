from random import shuffle

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import View, TemplateView

from geo_test.models import Quiz, Question


# should be template view which would display map
class QuizView(TemplateView):
    template_name = 'quiz.html'

    def get(self, request, *args, quiz_id=None, **kwargs):
        quiz = get_object_or_404(Quiz, pk=quiz_id)
        quiz_ids = list(quiz.questions.values_list('id', flat=True))
        shuffle(quiz_ids)

        if request.session.get('quiz_id', quiz_id) != quiz_id:
            return redirect(
                reverse('quiz', kwargs={'quiz_id': quiz_id})
            )

        request.session['quiz_id'] = quiz.id
        request.session['score'] = 0
        request.session['question_index'] = 0
        request.session['questions'] = quiz_ids

        context = self.get_context_data(**kwargs)
        context['quiz_name'] = quiz.name
        return self.render_to_response(context)


# should be rest api to not load every time question view and js map
class QuizQuestion(View):
    def get(self, request, quiz_id=None):
        # session is not initialized, start quiz by redirecting
        if self.request.session.get('quiz_id') != quiz_id:
            return redirect(reverse('quiz', kwargs={'quiz_id': quiz_id}))

        question_index = request.session['question_index']
        
        try:
            question_id = request.session['questions'][question_index]
        except IndexError:
            return JsonResponse({
                'errors': [{'message': 'Quiz finished'}]
            }, status=400)


        question = get_object_or_404(Question, pk=question_id)
        return JsonResponse({
            'data': {
                'question_id': question_id,
                'question_title': question.name,
                'question_number': question_index,
                'question_count': len(request.session['questions']),
                'question_progress': question_index/len(request.session['questions'])
            }
        })

    def post(self, request, quiz_id=None):
        request.session['question_index'] = request.session['question_index'] + 1


class QuizResult(TemplateView):
    # TODO will show result and save it to db for user if is logged
    # TODO v2 can redirect to logging if want to save result
    pass
