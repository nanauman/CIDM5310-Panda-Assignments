from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Venue(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)


def __str__(self):
    return self.title
