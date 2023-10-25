from django.db import models

# Create your models here.
class Uploads(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

def __str__(self):
    return self.title

class UploadFile(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='files')