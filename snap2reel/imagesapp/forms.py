from django import forms
from .models import MusicUpload

class MusicUploadForm(forms.ModelForm):
    class Meta:
        model = MusicUpload
        fields = ['music']
