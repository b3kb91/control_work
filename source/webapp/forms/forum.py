from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from webapp.models import Topic


class ForumForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')

        if not content:
            raise ValidationError('Поле для содержимого обязательно для заполнения')
        if not title:
            raise ValidationError('Поле для названия обязательно для заполнения')

        return cleaned_data

    class Meta:
        model = Topic
        fields = ['title', 'content']
        error_messages = {
            "title": {
                "required": "Поле обязательное"},
            "content": {
                "required": "Поле обязательное"},
        }
        widgets = {
            'content': widgets.Textarea(attrs={'cols': 23, "rows": 5})

        }
