import os
import shutil
from django import forms
from dejavu import Dejavu
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

djv = Dejavu(settings.DEJAVU_CONFIG)


class CreateAdvertForm(forms.Form):
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Advert title',
                                                                         'class': 'form-control'}))
    file = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    def clean_file(self):
        """ Validate file input for fingerprinting audio """
        file_obj = self.cleaned_data['file']
        path = default_storage.save('tmp/001.mp3', ContentFile(file_obj.read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)
        djv.fingerprint_file(tmp_file)

        return file_obj
