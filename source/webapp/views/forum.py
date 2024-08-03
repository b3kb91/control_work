from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView
from webapp.models import Topic, Answer
from webapp.forms import ReplyForm, ForumForm


class TopicListView(ListView):
    model = Topic
    template_name = 'forum/topic_list.html'
    ordering = ['-created_at']
    context_object_name = 'topics'
    paginate_by = 2


class TopicDetailView(ListView):
    model = Answer
    template_name = 'forum/topic_detail.html'
    context_object_name = 'answers'
    paginate_by = 2

    def get_queryset(self):
        topic = self.get_topic()
        return Answer.objects.filter(topic=topic).order_by('created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topic'] = self.get_topic()
        context['reply_form'] = ReplyForm()
        return context

    def get_topic(self):
        return Topic.objects.get(pk=self.kwargs['pk'])

    def post(self, request, *args, **kwargs):
        topic = self.get_topic()
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.topic = topic
            reply.user = request.user
            reply.save()
            return redirect('webapp:detail', pk=topic.pk)


class TopicCreateView(LoginRequiredMixin, CreateView):
    model = Topic
    form_class = ForumForm
    template_name = 'forum/topic_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
