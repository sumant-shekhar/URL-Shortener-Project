from django.db import models

# Create your models here.
class URL(models.Model):
    url = models.URLField(max_length=20000)
    uuid = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.uuid} -> {self.url}"

    