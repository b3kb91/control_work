from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from webapp.models import Photo


class PhotoListView(ListView):
    model = Photo
    template_name = 'photo/photo_list.html'
    ordering = ['-created_at']
    context_object_name = 'photos'
    paginate_by = 3


class PhotoDetailView(DetailView):
    template_name = "photo/detail_photo.html"
    model = Photo


class PhotoCreateView(CreateView):
    template_name = 'photo/create_photo.html'
    form_class = ''

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.save()
        photo.users.add(self.request.user)
        return super().form_valid(form)


class PhotoUpdateView(UpdateView):
    template_name = 'photo/update_photo.html'
    model = Photo
    form_class = ''


class PhotoDeleteView(DeleteView):
    template_name = 'photo/delete_photo.html'
    model = Photo
    success_url = reverse_lazy('webapp:main')
