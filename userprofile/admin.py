from django.contrib import admin
from .models import UserProfile, BookMark, Share

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_from', 'user_to', 'created']


class BookmarksAdmin(admin.ModelAdmin):
    list_display = ['user', 'poll', 'created']


class SharesAdmin(admin.ModelAdmin):
    list_display = ['user', 'poll', 'share_date']


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(BookMark, BookmarksAdmin)
admin.site.register(Share, SharesAdmin)