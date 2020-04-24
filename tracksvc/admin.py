from django.contrib import admin

# Register your models here.
from .models import Firearm,CheckEvent

admin.site.register(Firearm)
admin.site.register(CheckEvent)
