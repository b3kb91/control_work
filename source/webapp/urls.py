from django.template.context_processors import static
from django.urls import path

from webapp.views import TopicListView, TopicDetailView, TopicCreateView, AnswerUpdateView, AnswerDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', TopicListView.as_view(), name='main'),
    path('topic/<int:pk>/', TopicDetailView.as_view(), name='detail'),
    path('topic/create/', TopicCreateView.as_view(), name='create'),
    path('reply/<int:pk>/edit/', AnswerUpdateView.as_view(), name='answer_edit'),
    path('reply/<int:pk>/delete/', AnswerDeleteView.as_view(), name='answer_delete'),
]
