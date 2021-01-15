from django.contrib import admin
from .models import eventRegistration
from .models import participantRegistration

# Register your models here.

admin.site.register(eventRegistration)
admin.site.register(participantRegistration)
