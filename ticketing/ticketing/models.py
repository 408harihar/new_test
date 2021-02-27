from django.db import models


class Ticket(models.Model):
    submitter = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    hacker = models.CharField(max_length=100, blank=True)
