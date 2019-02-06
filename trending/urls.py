from django.urls import path, include, re_path
from trending.api import PollTrendingAPIListView


urlpatterns = [
    re_path('^polls/$', PollTrendingAPIListView.as_view(), name='trending-polls'),
]