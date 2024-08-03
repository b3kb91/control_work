from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from webapp.models import Answer


class AnswerUpdateView(UpdateView):
    model = Answer
    fields = ['content']
    template_name = 'answer/answer_update.html'

    def get_queryset(self):
        return Answer.objects.filter(user=self.request.user)


class AnswerDeleteView(DeleteView):
    model = Answer
    template_name = 'answer/answer_delete.html'
    success_url = reverse_lazy('webapp:main')

    def get_queryset(self):
        return Answer.objects.filter(user=self.request.user)
