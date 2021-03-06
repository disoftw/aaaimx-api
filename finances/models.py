from django.db import models
from uuid import uuid4
from datetime import datetime, timedelta
from productivity.models import Member
from django.contrib.postgres.fields import JSONField
from django.utils import timezone

# Create your models here.


class Invoice(models.Model):
    def __str__(self):
        return '{0}: ${1} - {2}'.format(self.type, self.amount, self.origin)
    origin = models.CharField(default="", max_length=100, blank=True)
    description = models.TextField(default="", blank=True)
    amount = models.FloatField(default=0, blank=True)
    type = models.CharField(default="", max_length=100, blank=True)
    voucher = models.URLField(default="", null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, editable=True, blank=True)


class Membership(models.Model):
    def __str__(self):
        return self.display_name
    member = models.ForeignKey(
        Member, null=True, blank=True, on_delete=models.SET_NULL)
    uuid = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    display_name = models.CharField(default="", max_length=200, blank=True)
    type = models.CharField(default="", max_length=50, blank=True)
    QR = models.URLField(default="", max_length=100, blank=True)
    exp = models.DateTimeField(default=timezone.now, blank=True)
    avatar = models.ImageField(upload_to='avatars', blank=True)
    file = models.ImageField(upload_to='memberships', blank=True)
    created_at = models.DateTimeField(auto_now=True, editable=False)
