from django.urls import path, include, re_path
from search.api import SearchPollAPIListView, SearchResultList


urlpatterns = [
    re_path('^polls/get/$', SearchPollAPIListView.as_view(), name='search-polls'),
    re_path('^polls/(?P<question>.+)/$', SearchResultList.as_view(), name='poll-searches'),

]