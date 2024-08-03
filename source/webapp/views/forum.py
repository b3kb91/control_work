from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from webapp.models import Topic
from webapp.forms import ReplyForm, ForumForm


class TopicListView(ListView):
    model = Topic
    template_name = 'forum/topic_list.html'
    ordering = ['-created_at']
    context_object_name = 'topics'
    paginate_by = 6


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        replies = self.object.replies.all()
        paginator = Paginator(replies, 5)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['reply_form'] = ReplyForm()
        context['page_obj'] = page_obj
        return context


class TopicCreateView(LoginRequiredMixin, CreateView):
    model = Topic
    form_class = ForumForm
    template_name = 'forum/topic_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
