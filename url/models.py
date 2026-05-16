from django.db import models


class Url(models.Model):
    link = models.URLField(blank=False)
    short_url = models.CharField(max_length=200)