from django.db import models

# Create your models here.
class ImageData(models.Model):
    name = models.CharField(max_length=100)
    discription = models.CharField(max_length=1000)
    id=models.IntegerField(default="",primary_key="id")
    cover_image = models.ImageField(upload_to="upasanaapp/images")
    def __str__(self):
        return self.name
class VideoData(models.Model):
    name = models.CharField(max_length=100)
    discription = models.CharField(max_length=1000)
    id=models.IntegerField(default="",primary_key="id")
    cover_image = models.ImageField(upload_to="upasanaapp/images",default='')
    file = models.FileField(upload_to='upasanaapp/videos/', null=True, verbose_name="")
    ytlink = models.CharField(max_length=100,default="")
    def __str__(self):
        return self.name
