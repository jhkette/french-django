from django.db import models
from datetime import datetime



# Create your models here.
class Vocabulary(models.Model):
    word = models.CharField(max_length=200)
    word_type = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date_published = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.word