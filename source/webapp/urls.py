from django.urls import path

from webapp.views import index, create_guestbook, update_guestbook

urlpatterns = [
    path('', index, name='main'),
    path('create/', create_guestbook, name='create'),
    path('guestbook/<int:pk>/update', update_guestbook, name='update')
]