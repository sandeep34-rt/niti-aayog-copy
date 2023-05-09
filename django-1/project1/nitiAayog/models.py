from django.db import models

# Create your models here.
class carousalImages(models.Model):
    img = models.ImageField(upload_to="nitiAayog/images",default="NIL")

    