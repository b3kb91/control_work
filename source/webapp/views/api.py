from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views import View
from webapp.models import Album, Photo


class ToggleFavoriteAlbumView(View, LoginRequiredMixin):
    def get(self, request, *args, pk, **kwargs):
        album = get_object_or_404(Album, pk=pk)

        if request.user in album.favorite_users.all():
            album.favorite_users.remove(request.user)
            is_favorite = False
        else:
            album.favorite_users.add(request.user)
            is_favorite = True
        return JsonResponse({'favorite': is_favorite})


class ToggleFavoritePhotoView(View, LoginRequiredMixin):
    def get(self, request, *args, pk, **kwargs):
        photo = get_object_or_404(Photo, pk=pk)

        if request.user in photo.favorite_users.all():
            photo.favorite_users.remove(request.user)
            is_favorite = False
        else:
            photo.favorite_users.add(request.user)
            is_favorite = True
        return JsonResponse({'favorite': is_favorite})
