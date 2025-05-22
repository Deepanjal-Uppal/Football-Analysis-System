from django import forms
from .models import VideoUpload

class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = VideoUpload
        # fields = ('title', 'video')  # Fields to be displayed in the form (video title and file)
        fields = ['video']  
