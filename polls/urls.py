from django.urls import path, include, re_path
# from .views import polls_list, polls_detail
from polls import api
from django.urls import path
from .views import ChoiceList, CreateVote, PollList, PollDetail

urlpatterns = [
    # path("polls/", polls_list, name="polls_list"),
    # path("polls/<int:pk>/", polls_detail, name="polls_details"),
    # re_path(r'^api/users$', api.UserCreate.as_view(), name='account-create'),
    # re_path('^poll/(?P<pk>[0-9]+)/$', api.PollAPIDetailView.as_view(), name='poll'),
    # re_path('^all-polls/$', api.PollAPIListView.as_view(), name='polls'),
    # re_path('^vote/(?P<pk>[0-9]+)/$', api.VotesAPIView.as_view(), name='vote'),
    # re_path('^votes/$', api.VoteAPIListView.as_view(), name='votes'),
    # re_path('^polls/(?P<pk>[0-9]+)/$', api.SinlgePOllAPIView.as_view(), name='each-poll')
]


urlpatterns = [
    path("<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    # path("choices/", ChoiceList.as_view(), name="choice_list"),
    # path("vote/", CreateVote.as_view(), name="create_vote"),
    path("polls/", PollList.as_view(), name="polls_list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail")
]