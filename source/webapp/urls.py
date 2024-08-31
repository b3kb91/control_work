from django.urls import path

from webapp.views import (PhotoListView, PhotoUpdateView, PhotoDeleteView, PhotoDetailView, PhotoCreateView,
                          AlbumUpdateView, AlbumListView, AlbumCreateView, AlbumDeleteView, AlbumDetailView,
                          AddFavoritePhotoView, AddFavoriteAlbumView, RemoveFavoritePhotoView, RemoveFavoriteAlbumView)

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

    path('photo/<int:photo_id>/add_favorite/', AddFavoritePhotoView.as_view(), name='add_favorite_photo'),
    path('photo/<int:photo_id>/remove_favorite/', RemoveFavoritePhotoView.as_view(), name='remove_favorite_photo'),
    path('album/<int:album_id>/add_favorite/', AddFavoriteAlbumView.as_view(), name='add_favorite_album'),
    path('album/<int:album_id>/remove_favorite/', RemoveFavoriteAlbumView.as_view(), name='remove_favorite_album'),
]
