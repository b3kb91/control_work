from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView
from webapp.models import Topic
from webapp.forms import ReplyForm, ForumForm


class TopicListView(ListView):
    model = Topic
    template_name = 'forum/topic_list.html'
    ordering = ['-created_at']
    context_object_name = 'topics'
    paginate_by = 1


class TopicDetailView(LoginRequiredMixin, DetailView):
    model = Topic
    template_name = 'forum/topic_detail.html'
    context_object_name = 'topic'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reply_form'] = ReplyForm()
        return context

    def post(self, request, *args, **kwargs):
        topic = self.get_object()
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.topic = topic
            reply.user = request.user
            reply.save()
            return redirect('webapp:main')


class TopicCreateView(LoginRequiredMixin, CreateView):
    model = Topic
    form_class = ForumForm
    template_name = 'forum/topic_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
