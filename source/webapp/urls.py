from django.urls import path

from webapp.views import (PhotoListView, PhotoUpdateView, PhotoDeleteView, PhotoDetailView, PhotoCreateView,
                          AlbumUpdateView, AlbumListView, AlbumCreateView, AlbumDeleteView, AlbumDetailView)

app_name = 'webapp'

urlpatterns = [
    path('', PhotoListView.as_view(), name='main'),
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name='delete_photo'),
    path('photo/<int:pk>/update/', PhotoUpdateView.as_view(), name='update_photo'),
    path('photo/create/', PhotoCreateView.as_view(), name='create_photo'),
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name='detail_photo'),

    path('album/', AlbumListView.as_view(), name='album'),
    path('album/<int:pk>/delete/', AlbumDeleteView.as_view(), name='delete_album'),
    path('album/<int:pk>/update/', AlbumUpdateView.as_view(), name='update_album'),
    path('album/create/', AlbumCreateView.as_view(), name='create_album'),
    path('album/<int:pk>/', AlbumDetailView.as_view(), name='detail_album'),
]
