from django.contrib import admin

# Register your models here.

from .models import AnonymousUserModel

admin.site.register(AnonymousUserModel)