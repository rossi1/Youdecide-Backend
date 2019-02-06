from django.urls import path, include, re_path
from feed.api import PollFeedAPIListView


urlpatterns = [
    re_path('^polls/$', PollFeedAPIListView.as_view(), name='feed-polls'),
]