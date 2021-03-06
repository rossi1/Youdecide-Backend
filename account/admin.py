from django.contrib import admin
#from .models import Profile
# users/admin.py
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User
# Register your models here.

"""

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['email', 'username',]


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']


# admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)
"""