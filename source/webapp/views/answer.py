from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from webapp.models import Answer


class AnswerUpdateView(UpdateView, LoginRequiredMixin):
    model = Answer
    fields = ['content']
    template_name = 'answer/answer_update.html'

    def has_permission(self):
        answer = self.get_object()
        return (self.request.user == answer.user or
                self.request.user.groups.filter(name='moderator').exists())


class AnswerDeleteView(DeleteView, LoginRequiredMixin):
    model = Answer
    template_name = 'answer/answer_delete.html'
    success_url = reverse_lazy('webapp:main')

    def get_queryset(self):
        return Answer.objects.filter(user=self.request.user)

    def has_permission(self):
        answer = self.get_object()
        return (self.request.user == answer.user or
                self.request.user.groups.filter(name='moderator').exists())
