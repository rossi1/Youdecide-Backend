from django.urls import path
from userprofile import api

urlpatterns = [

    path("<int:pk>/", api.SingleUserAPIDetailView.as_view(), name="user_detail"),
    path('update-profile/', api.UpdateUserProfiileAPIView.as_view(), name='update_profile'),
    path('bookmark-poll/', api.BookMarkAPIView.as_view(), name='bookmark'),
    path('share-poll/', api.SharesAPIView.as_view(), name='share'),
    path('like-poll/', api.LikesAPIView.as_view(), name='like'),
    path('delete-bookmark/<int:pk>/', api.DeleteBookMarkedAPIView.as_view(), name='delete_bookmark'),
    path('delete-share/<int:pk>/', api.DeleteSharesAPIView.as_view(), name='delete-share'),
    path('delete-like/<int:pk>/', api.DeleteLikesAPIView.as_view(), name='delete-like')
]