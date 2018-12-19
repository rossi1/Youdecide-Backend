# from django.contrib import admin
# from .models import Poll, Choices, PollDuration, Vote, ChoiceVotes
#
#
# # Register your models here.
# class ChoiceInline(admin.TabularInline):
#     model = Choices
#     extra = 0
#
#
# class PollAdmin(admin.ModelAdmin):
#     list_display = ['question', 'created_by', 'pub_date', 'expire_date', 'choice_type', 'slug']
#     list_filter = ('pub_date', 'question', 'created_by', 'choice_type')
#     search_fields = ('pub_date', 'question', 'created_by', 'choice_type')
#     prepopulated_fields = {'slug': ('question',)}
#     # # raw_id_fields = ('researcher',)
#     # date_hierarchy = 'created'
#     # ordering = ['created']
#     inlines = [ChoiceInline]
#
#
# class ChoicesVotesAdmin(admin.TabularInline):
#     list_display = ['voter', 'vote_count', 'choices']
#
#
# class ChoiceAdmin(admin.ModelAdmin):
#     list_display = ['choice_text', 'voter', 'vote_count']
#     inlines = [ChoicesVotesAdmin]
#
#
# # class PollDurationAdmin(admin.ModelAdmin):
#     # list_display = ['poll', 'expire_date']
#     # list_filter = ('expire_date', 'poll')
#     # search_fields = ('title', 'researcher')
#     # prepopulated_fields = {'slug': ('title',)}
#     # # raw_id_fields = ('researcher',)
#     # date_hierarchy = 'created'
#     # ordering = ['created']
#     # inlines = [CollaborateInLine]
#
#
# class VoteAdmin(admin.ModelAdmin):
#     list_display = ['choice', 'voter', 'vote_count']
#
#
# # admin.site.register(Poll, PollAdmin)
# # admin.site.register(Choices, ChoiceAdmin)
# # admin.site.register(PollDuration, PollDurationAdmin)
# admin.site.register(Vote, VoteAdmin)
# admin.site.register(Poll, PollAdmin)
# # admin.site.register(ChoiceVotes, ChoicesVotesAdmin)
