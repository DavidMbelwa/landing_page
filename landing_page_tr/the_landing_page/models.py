from django.db import models

# Create your models here.
class Kurslar(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="imgs/")
    description = models.TextField(blank=True)