from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
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
        if self.request.user.is_authenticated:
            return Photo.objects.filter(is_public=True).order_by('-created_at')
        return Photo.objects.filter(is_public=True).order_by('-created_at')


class PhotoDetailView(DetailView):
    template_name = "photo/detail_photo.html"
    model = Photo

    def get_object(self):
        photo = super().get_object()
        if not photo.is_public and photo.author != self.request.user:
            raise PermissionDenied
        return photo


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


class PhotoUpdateView(UpdateView):
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


class PhotoDeleteView(DeleteView):
    template_name = 'photo/delete_photo.html'
    model = Photo
    context_object_name = 'photo'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Photo.objects.filter(author=self.request.user)
