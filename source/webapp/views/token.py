from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseForbidden
from webapp.models import Photo


def photo_by_token(request, token):
    photo = get_object_or_404(Photo, token=token)
    if not photo.is_public and photo.author != request.user:
        return HttpResponseForbidden("Вы не имеете доступа к этому фото.")
    return render(request, 'photo/detail_photo.html', {'photo': photo})
