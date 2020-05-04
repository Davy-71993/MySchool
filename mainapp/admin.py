from django.contrib import admin
from .models import Calendar, Event, Term

admin.site.register(Calendar)
admin.site.register(Event)
admin.site.register(Term)

# Register your models here.
