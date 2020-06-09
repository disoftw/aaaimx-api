from django.db import models
from uuid import uuid4
from datetime import datetime
from productivity.models import Division
from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()

# Create your models here.
class Event(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=100, null=True, default="")
    date_start = models.DateTimeField(blank=True)
    date_end = models.DateTimeField(blank=True)
    description = models.TextField(default="", blank=True)
    type = models.CharField(max_length=100, blank=True)
    division = models.ForeignKey(Division, null=True, blank=True, on_delete=models.SET_NULL)
    place = models.CharField(max_length=100, blank=True)
    flyer = models.ImageField(
        default=None, null=True, blank=True, upload_to='flyers')

class Certificate(models.Model):
    def __str__(self):
        return '{0}: {1}'.format(self.type, self.to)
    uuid = models.UUIDField(default=uuid4, primary_key=True, editable=True)
    type = models.CharField(max_length=100, default="RECOGNITION", blank=True,)
    published = models.BooleanField(default=False)
    to = models.CharField(max_length=100, blank=True, default="")
    QR = models.CharField(max_length=100, blank=True, default='www.aaaimx.org/certificates/?id=')
    file = models.ImageField(upload_to='certs', blank=True, storage=gd_storage)
    description = models.TextField(default="", blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True, null=True)


class Component(models.Model):
    def __str__(self):
        return self.description
    description = models.CharField(default="", max_length=200, blank=True)
    stock = models.IntegerField(default=0, blank=True)
    available = models.IntegerField(default=0, blank=True)
    observations = models.TextField(default="", blank=True)
