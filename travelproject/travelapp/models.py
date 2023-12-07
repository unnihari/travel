from django.db import models


# Create your models here.
class place(models.Model):
    objects = None
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    dec = models.TextField()

    def __str__(self):
        return self.name




