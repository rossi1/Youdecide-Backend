from django.contrib import admin
from .models import Poll, Choice


# Register your models here.
class PollAdmin(admin.ModelAdmin):
    list_display = ['question', 'created_by', 'pub_date']


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['poll', 'choice_text']


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
