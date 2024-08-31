import uuid

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from webapp.forms import PhotoForm
from webapp.models import Photo


class PhotoListView(ListView):
    model = Photo
    template_name = 'photo/photo_list.html'
    ordering = ['-created_at']
    context_object_name = 'photos'
    paginate_by = 3

    def get_queryset(self):
        return Photo.objects.filter(is_public=True).order_by('-created_at')


class PhotoDetailView(DetailView, LoginRequiredMixin):
    template_name = "photo/detail_photo.html"
    model = Photo

    def get_object(self):
        token = self.kwargs.get('token')
        if token:
            try:
                photo = get_object_or_404(Photo, token=uuid.UUID(token))
            except ValueError:
                raise PermissionDenied("Недопустимый токен")
        else:
            photo = super().get_object()
        if not photo.is_public and photo.author != self.request.user:
            raise PermissionDenied

        return photo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photo = self.object
        context['is_owner'] = photo.author == self.request.user
        context['link'] = reverse('webapp:photo_by_token', kwargs={'token': photo.token}) if photo.token else None
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author != request.user or self.object.token:
            return HttpResponseForbidden("не можете генерировать ссылку для этого фото")
        self.object.token = uuid.uuid4()
        self.object.save()
        return HttpResponseRedirect(self.get_object().get_absolute_url())


class PhotoCreateView(CreateView, LoginRequiredMixin):
    template_name = 'photo/create_photo.html'
    form_class = PhotoForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class PhotoUpdateView(UpdateView, LoginRequiredMixin):
    template_name = 'photo/update_photo.html'
    model = Photo
    form_class = PhotoForm

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Photo.objects.filter(author=self.request.user)


class PhotoDeleteView(DeleteView, LoginRequiredMixin):
    template_name = 'photo/delete_photo.html'
    model = Photo
    context_object_name = 'photo'
    success_url = reverse_lazy('webapp:main')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Photo.objects.filter(author=self.request.user)

