from django.urls import path, include, re_path
# from .views import polls_list, polls_detail
from polls import api
from django.urls import path
from userprofile.api import SingleUserAPIDetailView



urlpatterns = [

    path("/<int:pk>/", SingleUserAPIDetailView.as_view(), name="user_detail")
]