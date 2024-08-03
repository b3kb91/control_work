from django.urls import path

from webapp.views import TopicListView, TopicDetailView, TopicCreateView

app_name = 'webapp'

urlpatterns = [
    path('', TopicListView.as_view(), name='main'),
    path('topic/<int:pk>/', TopicDetailView.as_view(), name='detail'),
    path('topic/create/', TopicCreateView.as_view(), name='create'),
]
