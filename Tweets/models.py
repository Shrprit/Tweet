from django.db import models

# Create your models here.
class tweet(models.Model):
    content = models.TextField(blank=True,null=True)
    images = models.FileField(upload_to='images/',blank=True,null=True)
