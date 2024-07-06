from django.urls import path

from webapp.views import index, create_guestbook

urlpatterns = [
    path('', index, name='main'),
    path('create/', create_guestbook, name='create'),
]