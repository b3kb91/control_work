from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from webapp.models import Topic, Answer


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'forum/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        topics = Topic.objects.filter(user=user)
        context['user'] = user
        context['topics'] = topics
        context['reply_count'] = Answer.objects.filter(user=user).count()
        return context
