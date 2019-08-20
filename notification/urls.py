from django.urls import path

from . import views

urlpatterns = [
    path('', views.NotificationUnreadListView.as_view(), name='unread'),
    path('mark-as-read/<slug:slug>/', views.mark_as_read, name='mark_as_read'),
    path('mark-all-as-read/', views.mark_all_as_read, name='mark_all_read'),
    path('latest-notifications/', views.get_latest_notifications, name='latest_notifications'),
]
