from django.urls import path

from webapp.views.photo import PhotoListView

app_name = 'webapp'

urlpatterns = [
    path('', PhotoListView.as_view(), name='main'),
    # path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='delete_project'),
    # path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='update_project'),
    # path('project/create/', ProjectCreateView.as_view(), name='create_project'),
    # path('project/<int:pk>/', ProjectDetailView.as_view(), name='detail_project'),
    # path('issue/<int:pk>/', IssueDetailView.as_view(), name="detail"),
    # path('issue/<int:pk>/update/', IssueUpdateView.as_view(), name='update'),
    # path('issue/<int:pk>/create/', IssueCreateView.as_view(), name='create'),
    # path('delete/<int:pk>/', IssueDeleteView.as_view(), name="delete"),
]