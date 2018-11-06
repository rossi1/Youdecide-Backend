from django.contrib import admin
from .models import PostPoll, QuestionGroups, Questions, UserVotes, Answers


# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Questions._meta.get_fields()]


class AnswerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Answers._meta.get_fields()]


class PollAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PostPoll._meta.get_fields()]


class QuestionGroupAdmin(admin.ModelAdmin):
    list_display = [field.name for field in QuestionGroups._meta.get_fields()]


class UserVotesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserVotes._meta.get_fields()]


admin.site.register(Questions, QuestionAdmin)
admin.site.register(Answers, AnswerAdmin)
admin.site.register(PostPoll, PollAdmin)
admin.site.register(UserVotes, UserVotesAdmin)
admin.site.register(QuestionGroups, QuestionGroupAdmin)
