from django.urls import path

from webapp.views import (PhotoListView, PhotoUpdateView, PhotoDeleteView, PhotoDetailView, PhotoCreateView,
                          AlbumUpdateView, AlbumListView, AlbumCreateView, AlbumDeleteView, AlbumDetailView,
                          ToggleFavoritePhotoView, ToggleFavoriteAlbumView, photo_by_token)

app_name = 'webapp'

urlpatterns = [
    path('', PhotoListView.as_view(), name='main'),
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name='delete_photo'),
    path('photo/<int:pk>/update/', PhotoUpdateView.as_view(), name='update_photo'),
    path('photo/create/', PhotoCreateView.as_view(), name='create_photo'),
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name='detail_photo'),
    path('photo/<int:pk>/generate_token/', PhotoDetailView.as_view(), name='generate_token'),

    path('album/', AlbumListView.as_view(), name='album'),
    path('album/<int:pk>/delete/', AlbumDeleteView.as_view(), name='delete_album'),
    path('album/<int:pk>/update/', AlbumUpdateView.as_view(), name='update_album'),
    path('album/create/', AlbumCreateView.as_view(), name='create_album'),
    path('album/<int:pk>/', AlbumDetailView.as_view(), name='detail_album'),

    path('album/<int:pk>/toggle_favorite/', ToggleFavoriteAlbumView.as_view(), name='toggle_favorite_album'),
    path('photo/<int:pk>/toggle_favorite/', ToggleFavoritePhotoView.as_view(), name='toggle_favorite_photo'),

    path('photo/token/<uuid:token>/', photo_by_token, name='photo_by_token'),
]
