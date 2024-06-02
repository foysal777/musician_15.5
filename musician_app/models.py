from django.db import models

# Create your models here.
from django.db import models
from album_app.models import albumModel

class musicModel(models.Model):
    musician_id = models.IntegerField(primary_key=True, default=1)
    musicians = models.ForeignKey(albumModel, on_delete=models.CASCADE, default=1)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.IntegerField()
    instrument = models.CharField(max_length=40)

    def __str__(self):
        return self.first_name