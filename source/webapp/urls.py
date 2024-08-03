from django.urls import path

from webapp.views import TopicListView, TopicDetailView, TopicCreateView, AnswerUpdateView, AnswerDeleteView
from webapp.views.personal import ProfileView

app_name = 'webapp'

urlpatterns = [
    path('', TopicListView.as_view(), name='main'),
    path('topic/<int:pk>/', TopicDetailView.as_view(), name='detail'),
    path('topic/create/', TopicCreateView.as_view(), name='create'),
    path('reply/<int:pk>/edit/', AnswerUpdateView.as_view(), name='answer_edit'),
    path('reply/<int:pk>/delete/', AnswerDeleteView.as_view(), name='answer_delete'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
