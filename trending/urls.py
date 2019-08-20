from django.urls import path, include, re_path
from trending.api import PollTrendingAPIListView, PollFeed


urlpatterns = [
    re_path('^polls/$', PollTrendingAPIListView.as_view(), name='trending-polls'),
    path('feed/', PollFeed.as_view(), name='pol_feed')
]