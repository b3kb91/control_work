from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from webapp.models import Topic
from webapp.forms import ForumForm


class TopicListView(ListView):
    model = Topic
    template_name = 'forum/topic_list.html'
    ordering = ['-created_at']
    context_object_name = 'topics'


class TopicDetailView(DetailView):
    model = Topic
    template_name = 'forum/topic_detail.html'
    context_object_name = 'topic'


class TopicCreateView(CreateView):
    model = Topic
    form_class = ForumForm
    template_name = 'forum/topic_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
