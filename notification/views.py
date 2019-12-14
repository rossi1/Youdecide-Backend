from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Notification
from .serializers import NotificationSerializer


class NotificationUnreadListView(ListAPIView):
    """Basic ListView implementation to show the unread notifications for
    the actual user"""
    queryset = Notification
    serializer_class = NotificationSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, **kwargs):
        return self.request.user.notifications.unread()




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def mark_all_as_read(request):
    """View to call the model method which marks as read all the notifications
    directed to the actual user."""
    request.user.notifications.mark_all_as_read()
    msg = "All notifications to {} have been marked as read.".format(str(request.user.username))

    return Response(data=msg, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def mark_as_read(request, slug=None):
    """View to call the model method which mark as read the provided
    notification."""
    if slug:
        notification = get_object_or_404(Notification, slug=slug)
        notification.mark_as_read()

    msg = "The notification {} has been marked as read.".format(notification.slug)

    return Response(data=msg, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_latest_notifications(request):
    notifications = request.user.notifications.get_most_recent()
    recent_notify = [notifs for notifs in notifications]
    return Response(data=recent_notify, status=status.HTTP_200_OK)
