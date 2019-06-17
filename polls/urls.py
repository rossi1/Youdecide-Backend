from django.urls import path, include, re_path
# from .views import polls_list, polls_detail

from django.urls import path, include

from rest_framework import routers

from polls import api
from .views import ChoiceList, CreateVote, PollList, PollDetail, PollCreate, PollDocumentView

router = routers.SimpleRouter()

router.register('', PollDocumentView)

urlpatterns = [
    path("<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    # path("choices/", ChoiceList.as_view(), name="choice_list"),
    path("vote/<int:pk>/<int:choice_pk>/", CreateVote.as_view(), name="create_vote"),
    path("polls/", PollList.as_view(), name="polls_list"),
    path("create-polls", PollCreate.as_view(), name='poll_create'),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("search/", include(router.urls), name="poll_search")
]