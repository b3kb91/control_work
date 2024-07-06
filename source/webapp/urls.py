from django.urls import path

from webapp.views import index, create_guestbook, update_guestbook, delete_guestbook

urlpatterns = [
    path('', index, name='main'),
    path('create/', create_guestbook, name='create'),
    path('guestbook/<int:pk>/update', update_guestbook, name='update'),
    path('guestbook/<int:pk>/', delete_guestbook, name='delete')

]
