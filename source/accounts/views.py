from django.contrib.auth import login, get_user_model
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from webapp.models import Album, Photo

from accounts.forms import UserRegisterForm

User = get_user_model()


class RegistrationView(CreateView):
    form_class = UserRegisterForm
    template_name = 'registration.html'
    model = User

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')

        if not next_url:
            next_url = self.request.POST.get('next')

        if not next_url:
            next_url = reverse('webapp:main')

        return next_url


class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'profile_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object
        current_user = user == self.request.user

        context['public_albums'] = Album.objects.filter(author=user, is_public=True)
        context['public_photos'] = Photo.objects.filter(author=user, album__isnull=True, is_public=True)

        if current_user:
            context['private_albums'] = Album.objects.filter(author=user, is_public=False)
            context['private_photos'] = Photo.objects.filter(author=user, album__isnull=True, is_public=False)

            favorite_album_ids = user.favorite_albums.values_list('id', flat=True)
            context['favorites'] = Photo.objects.filter(id__in=user.favorite_photos.values_list('id', flat=True))
            context['favorite_albums'] = Album.objects.filter(id__in=favorite_album_ids)

        return context

