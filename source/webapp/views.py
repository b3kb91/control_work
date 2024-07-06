from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import GuestBookForm
from webapp.models import GuestBook


def index(request):
    guest_book = GuestBook.objects.order_by("-creation_time")
    return render(request, 'index.html', context={'guest_book': guest_book})


def create_guestbook(request):
    if request.method == "GET":
        form = GuestBookForm()
        return render(request, 'create_guestbook.html', context={'form': form})
    else:
        form = GuestBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')

        return render(
            request,
            'create_guestbook.html',
            {"form": form}

        )

