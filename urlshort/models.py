from django.db import models

class Link(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True)

