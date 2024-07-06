from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from webapp.forms import GuestBookForm
from webapp.models import GuestBook


def index(request):
    if request.method == 'GET':
        form = SearchGuestBook(request.GET)
        if form.is_valid():
            author_name = form.cleaned_data['name']
            guestbook = GuestBook.objects.filter(status='active', name__icontains=author_name).order_by("-creation_time")
        else:
            guestbook = GuestBook.objects.filter(status='active').order_by("-creation_time")
    else:
        form = SearchGuestBook()
        guestbook = GuestBook.objects.filter(status='active').order_by("-creation_time")
    return render(request, 'index.html', context={'form': form, 'guest_book': guestbook})


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


def update_guestbook(request, pk):
    guestbook = get_object_or_404(GuestBook, pk=pk)
    if request.method == "GET":
        form = GuestBookForm(instance=guestbook)
        return render(
            request,
            'guestbook_update.html',
            context={'form': form}
        )
    else:
        form = GuestBookForm(request.POST, instance=guestbook)
        if form.is_valid():
            form.save()
            return redirect('main')

        return render(
            request,
            'guestbook_update.html',
            context={'form': form}
        )


def delete_guestbook(request, *args, pk, **kwargs):
    guestbook = get_object_or_404(GuestBook, pk=pk)
    if request.method == "POST":
        email_del = request.POST.get('email')
        if email_del == guestbook.email:
            guestbook.delete()
            return redirect('main')
        else:
            messages.error(request, "Неправильно введено, попробуйте еще раз")
    return render(request, "delete_guestbook.html", context={"guestbook": guestbook})

