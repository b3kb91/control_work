from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.core.exceptions import PermissionDenied

from webapp.models import Album
from webapp.forms import AlbumForm


class AlbumListView(ListView):
    model = Album
    template_name = 'album/album_list.html'
    context_object_name = 'albums'
    paginate_by = 3

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Album.objects.filter(is_public=True).order_by('-created_at')
        return Album.objects.filter(is_public=True).order_by('-created_at')


class AlbumDetailView(DetailView):
    model = Album
    template_name = 'album/album_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        album = self.get_object()
        context['photos'] = album.get_photos()
        return context


class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album/album_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AlbumUpdateView(LoginRequiredMixin, UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album/album_update.html'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class AlbumDeleteView(LoginRequiredMixin, DeleteView):
    model = Album
    template_name = 'album/album_delete.html'
    context_object_name = 'album'

    def delete(self, request, *args, **kwargs):
        album = self.get_object()
        album.photo_set.all().delete()
        return super().delete(request, *args, **kwargs)
