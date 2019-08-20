from django.contrib import admin
from .models import Profile, BookMark, Share, Likes

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_from', 'user_to', 'created']


class BookmarksAdmin(admin.ModelAdmin):
    list_display = ['user', 'poll', 'created']


class SharesAdmin(admin.ModelAdmin):
    list_display = ['user', 'poll', 'share_date']

class LikesAdmin(admin.ModelAdmin):
    list_display = ['user', 'poll', 'like_date']


admin.site.register(Profile)
admin.site.register(BookMark, BookmarksAdmin)
admin.site.register(Share, SharesAdmin)
admin.site.register(Likes, LikesAdmin)