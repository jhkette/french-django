from django.contrib import admin

# Register your models here.
from .models import Programme

class ProgrammeAdmin(admin.ModelAdmin):
    pass
  
admin.site.register(Programme, ProgrammeAdmin)

