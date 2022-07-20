from pyexpat import model
from statistics import mode
from tabnanny import verbose
from django.db import models

# Create your models here.
class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text

class Entry(models.Model):
    """Something specific learned about topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

        def  __str__(self) -> str:
            """Return a string repersentation of a model."""
            return f"{self.text[:50]}..."