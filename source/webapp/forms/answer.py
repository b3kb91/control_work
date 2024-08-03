from django import forms
from django.forms import widgets

from webapp.models import Answer


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        error_messages = {
            "content": {
                "required": "Поле обязательное"},
        }
        widgets = {
            'content': widgets.Textarea(attrs={'cols': 50, "rows": 5})
        }
