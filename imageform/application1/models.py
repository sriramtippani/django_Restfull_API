from django.db import models

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=50)
    document = models.FileField(upload_to='', null=True, verbose_name="")
    uploaded_at = models.DateTimeField(auto_now_add=True)
