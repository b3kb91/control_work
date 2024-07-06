from django import forms
from django.core.exceptions import ValidationError

from webapp.models import GuestBook
from django.forms import widgets


class GuestBookForm(forms.ModelForm):
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) <= 3:
            raise ValidationError("Слишком короткое имя, попробуйте подлиннее")
        else:
            return name

    class Meta:
        model = GuestBook
        fields = ['name', 'email', 'text']
        error_messages = {
            'name': {
                'required': 'Обязательное поле'
            },
            'email': {
                'required': 'Обязательное поле'
            },
            'text': {
                'required': 'Обязательное поле'
            }
        }
        widgets = {
            'text': widgets.Textarea(attrs={'cols': 20, 'rows': 5}),
        }


class SearchGuestBook(forms.Form):
    name = forms.CharField(label='Имя автора', max_length=200, required=False)
