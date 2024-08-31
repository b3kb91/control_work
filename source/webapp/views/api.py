from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views import View
from django.contrib.auth import get_user_model
from webapp.models import Album, Photo


class ToggleFavoriteAlbumView(View):
    def post(self, request, *args, **kwargs):
        album = get_object_or_404(Album, pk=self.kwargs['pk'])
        if request.user in album.favorite_users.all():
            album.favorite_users.remove(request.user)
            is_favorite = False
        else:
            album.favorite_users.add(request.user)
            is_favorite = True

        if request.is_ajax():
            return JsonResponse({'success': True, 'is_favorite': is_favorite})
        return JsonResponse({'success': True, 'is_favorite': is_favorite})


class ToggleFavoritePhotoView(View):
    def post(self, request, *args, **kwargs):
        photo = get_object_or_404(Photo, pk=self.kwargs['pk'])
        if request.user in photo.favorite_users.all():
            photo.favorite_users.remove(request.user)
            is_favorite = False
        else:
            photo.favorite_users.add(request.user)
            is_favorite = True

        if request.is_ajax():
            return JsonResponse({'success': True, 'is_favorite': is_favorite})
        return JsonResponse({'success': True, 'is_favorite': is_favorite})
