from django.urls import path, include, re_path
# from .views import polls_list, polls_detail
from polls import api
from feed.api import PollFeedAPIListView


urlpatterns = [
    # re_path('^poll/(?P<pk>[0-9]+)/$', api.PollAPIDetailView.as_view(), name='poll'),
    re_path('^polls/get/$', PollFeedAPIListView.as_view(), name='polls-feed'),
]