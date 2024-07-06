from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import GuestBook


def index(request):
    guest_book = GuestBook.objects.order_by("-creation_time")
    return render(request, 'index.html', context={'guest_book': guest_book})


def create_guestbook(request):
    pass
