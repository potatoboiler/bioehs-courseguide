from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
import datetime
from PIL import Image

# Create your models here.

class Year(models.Model):
    year = models.PositiveSmallIntegerField(default = datetime.datetime.now().year)
    def __str__(self):
        return str(self.year)
    class Meta:
        ordering = ['year']

class Sponsor(models.Model):
    """ Model representing a company. """
    name = models.CharField(max_length=100, help_text='Enter Sponsor Name here.')
    year = models.ManyToManyField(Year, related_name='sponsors')
    pic = models.ImageField(upload_to = 'sponsors/', default = 'sponsors/default.png', editable=True)
    # image = Image.open(pic.path)
    link = models.URLField(blank=True)
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
