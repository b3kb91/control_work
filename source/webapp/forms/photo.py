from django import forms
from rest_framework.exceptions import ValidationError

from webapp.models import Photo, Album


class PhotoForm(forms.ModelForm):

    def clean_photo(self):
        photo = self.cleaned_data['photo']
        if not photo:
            raise ValidationError('Фотография не может быть пустой')
        return photo

    def clean_signature(self):
        signature = self.cleaned_data['signature']
        if not signature:
            raise ValidationError('Подпись не может быть пустой')
        return signature

    class Meta:
        model = Photo
        fields = ['photo', 'signature', 'album', 'is_public']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user and self.user.is_authenticated:
            self.fields['album'].queryset = Album.objects.filter(author=self.user)

        else:
            self.fields['album'].queryset = Album.objects.none()

    def clean(self):
        cleaned_data = super().clean()
        album = cleaned_data.get('album')
        is_public = cleaned_data.get('is_public')

        if album and not album.is_public and is_public:
            raise ValidationError("Нельзя сделать фотографию публичной, если она в приватном альбоме")
        return cleaned_data
