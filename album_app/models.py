from django.db import models
# from musician_app.models import m_model


class albumModel(models.Model):
    Album_name = models.CharField(max_length=100)  
    Album_release_Date = models.DateTimeField(("Release Date"), auto_now=True)   
    RATING_CHOICES = [
        (1, '1 '),
        (2, '2'),
        (3, '3 '),
        (4, '4'),
        (5, '5'),
    ]  
    Album_Rating = models.IntegerField(("Rating"), choices=RATING_CHOICES)
    def __str__(self):
        return self.Album_name