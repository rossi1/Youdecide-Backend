from django.urls import path
from userprofile.api import SingleUserAPIDetailView


urlpatterns = [

    path("<int:pk>/", SingleUserAPIDetailView.as_view(), name="user_detail")
]