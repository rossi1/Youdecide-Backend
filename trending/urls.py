from django.urls import path, include, re_path

from trending.api import PollTrendingAPIListView


urlpatterns = [
    # re_path('^poll/(?P<pk>[0-9]+)/$', api.PollAPIDetailView.as_view(), name='poll'),
    re_path('^polls/get/$', PollTrendingAPIListView.as_view(), name='polls-trending'),
]