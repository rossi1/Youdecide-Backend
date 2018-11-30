from django.urls import path, include, re_path
# from .views import polls_list, polls_detail
from polls import api


urlpatterns = [
    # path("polls/", polls_list, name="polls_list"),
    # path("polls/<int:pk>/", polls_detail, name="polls_details"),
#re_path(r'^api/users$', api.UserCreate.as_view(), name='account-create'),
    re_path('^poll/(?P<pk>[0-9]+)/$', api.PollAPIDetailView.as_view(), name='poll'),
    re_path('^all-polls/$', api.PollAPIListView.as_view(), name='polls'),
]