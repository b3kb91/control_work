from django.http import JsonResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from webapp.models import Photo, Album, FavoritePhoto, FavoriteAlbum


class AddFavoritePhotoView(LoginRequiredMixin, View):
    def post(self, request, pk):
        try:
            photo = Photo.objects.get(pk=pk)
            if not FavoritePhoto.objects.filter(user=request.user, photo=photo).exists():
                FavoritePhoto.objects.create(user=request.user, photo=photo)
                return JsonResponse({'success': True, 'action': 'added'})
            return JsonResponse({'success': False, 'error': 'Photo already in favorites'}, status=400)
        except Photo.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Photo not found'}, status=404)


class RemoveFavoritePhotoView(LoginRequiredMixin, View):
    def delete(self, request, pk):
        try:
            photo = Photo.objects.get(pk=pk)
            favorite = FavoritePhoto.objects.filter(user=request.user, photo=photo).first()
            if favorite:
                favorite.delete()
                return JsonResponse({'success': True, 'action': 'removed'})
            return JsonResponse({'success': False, 'error': 'Photo not in favorites'}, status=400)
        except Photo.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Photo not found'}, status=404)


class AddFavoriteAlbumView(LoginRequiredMixin, View):
    def post(self, request, pk):
        try:
            album = Album.objects.get(pk=pk)
            if not FavoriteAlbum.objects.filter(user=request.user, album=album).exists():
                FavoriteAlbum.objects.create(user=request.user, album=album)
                return JsonResponse({'success': True, 'action': 'added'})
            return JsonResponse({'success': False, 'error': 'Album already in favorites'}, status=400)
        except Album.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Album not found'}, status=404)


class RemoveFavoriteAlbumView(LoginRequiredMixin, View):
    def delete(self, request, pk):
        try:
            album = Album.objects.get(pk=pk)
            favorite = FavoriteAlbum.objects.filter(user=request.user, album=album).first()
            if favorite:
                favorite.delete()
                return JsonResponse({'success': True, 'action': 'removed'})
            return JsonResponse({'success': False, 'error': 'Album not in favorites'}, status=400)
        except Album.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Album not found'}, status=404)
