from django.db import models

class ImageUpload(models.Model):
    image = models.ImageField(upload_to='uploads/images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class MusicUpload(models.Model):
    music = models.FileField(upload_to='uploads/music/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
