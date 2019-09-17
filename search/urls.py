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
    path("poll", include(router.urls), name="poll_search")

]
"""




#from django.conf.urls import patterns, url, include
#from rest_framework import routers
#from django.urls import include , path 

#from .views import PollSearchView

#router = routers.DefaultRouter()
#router.register("", PollSearchView, base_name="poll-search")

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PollDocumentView

router = DefaultRouter()
router.register(r'',  PollDocumentView, basename='polldocument')


urlpatterns = [


    path("poll/", include(router.urls))

]