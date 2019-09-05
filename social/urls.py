from django.urls import path

from . import api


urlpatterns = [
    path('follow-user/', api.FollowUserAPIView.as_view(), name='follow_user'),
    path('followers/', api.ListFollowersAPIView.as_view(), name='followers'),
    path('followings/', api.ListFollowingAPIView.as_view(), name='followings'),
    path('unfollow-user/<str:id>/', api.UnfollowAPIView.as_view(), name='unfollow')
]