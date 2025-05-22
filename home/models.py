from django.db import models

# Create your models here.
class VideoUpload(models.Model):
    # title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')  # Uploaded video will be stored in 'media/videos/'

    # def _str_(self):
        # return self.title
    
