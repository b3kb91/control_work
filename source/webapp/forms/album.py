from django import forms
from webapp.models import Album
from django.forms import widgets


class AlbumForm(forms.ModelForm):

    def clean_title(self):
        title = self.cleaned_data['title']
        if not title:
            raise title('Название не может быть пустой')
        return title

    class Meta:
        model = Album
        fields = ['title', 'description', 'is_public']
        error_messages = {
            "title": {
                "required": "Поле обязательное"},

        }
        widgets = {
            'description': widgets.Textarea(attrs={'cols': 20, "rows": 5}),

        }
