from django.contrib import admin

# Register your models here.
from .models import Vocabulary


class VocabAdmin(admin.ModelAdmin):
    pass
  
admin.site.register(Vocabulary, VocabAdmin)