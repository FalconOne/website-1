from django.db import models
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64, blank=True)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=64, blank=True)
    subject = models.CharField(max_length=255)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class meta:
        ordering = ['created_at']
    def __str__(self):
        return self.first_name