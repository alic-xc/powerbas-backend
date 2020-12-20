from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
# Create your views here.


from django.views import generic

from fingerprints.forms import CreateAdvertForm


class AdvertDetailtView(generic.DetailView):
    pass


class AdvertListView(generic.ListView):
    pass


class CreateAdvertView(generic.FormView):
    template_name = 'fingerprints/add-advert.html'
    form_class = CreateAdvertForm

    def form_valid(self, form):
        path = default_storage.save('tmp/somename.mp3', ContentFile())

        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)
