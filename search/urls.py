
"""
from django.urls import path, include, re_path

from rest_framework import routers

from search.api import ( SearchPollAPIListView, SearchResultList, SearchPollHistoriesAPIListView,
                         SearchPollHistoryAPIDetailView, FailedSearchesAPIListView)

from .views import PollDocumentSearchView

router = routers.SimpleRouter()

router.register('', PollDocumentSearchView)

urlpatterns = [
    re_path('^polls/get/$', SearchPollAPIListView.as_view(), name='search-polls'),
    re_path('^polls/(?P<question>.+)/$', SearchResultList.as_view(), name='poll-searches'),
    re_path('^polls/histories/$', SearchPollHistoriesAPIListView.as_view(), name='search-poll-histories'),
    re_path('^polls/(?P<id>.+)/$', SearchPollHistoriesAPIListView.as_view(), name='search-poll-history'),
    re_path('^failed-searches/', FailedSearchesAPIListView.as_view(), name='failed-searches'),
    path("search/", include(router.urls), name="poll_search")

]
"""
