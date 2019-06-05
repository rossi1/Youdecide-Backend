from django.contrib import admin

# Register your models here.

from .models import AnonymousVoter

admin.site.register(AnonymousVoter)