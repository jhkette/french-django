from django.db import models
from vocabulary.models import Vocabulary
from datetime import datetime


# Create your models here.

class Programme(models.Model):
    progamme = models.CharField(max_length=200)
    vocabulary = models.ForeignKey(Vocabulary, on_delete=models.DO_NOTHING)
    description = models.TextField(blank=True)
    date_published = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.progamme