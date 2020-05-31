from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length= 100)
    body = models.CharField(max_length=1000)
    img = models.ImageField(upload_to = "blog/image")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)