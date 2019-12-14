import uuid
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core import serializers
from django.db import models
from django.utils.translation import ugettext_lazy as _

from social.models import Follow
#from asgiref.sync import async_to_sync
#from channels.layers import get_channel_layer
#from slugify import slugify


class NotificationQuerySet(models.query.QuerySet):
    """Personalized queryset created to improve model usability"""

    def unread(self):
        """Return only unread items in the current queryset"""
        return self.filter(unread=True)

    def read(self):
        """Return only read items in the current queryset"""
        return self.filter(unread=False)

    def mark_all_as_read(self, poll_viewers=None):
        """Mark as read any unread elements in the current queryset with
        optional filter by poll_viewers first.
        """
        qs = self.unread()
        if poll_viewers:
            qs = qs.filter(poll_viewers=poll_viewers)

        return qs.update(unread=False)

    def mark_all_as_unread(self, poll_viewers=None):
        """Mark as unread any read elements in the current queryset with
        optional filter by poll_viewers first.
        """
        qs = self.read()
        if poll_viewers:
            qs = qs.filter(poll_viewers=poll_viewers)

        return qs.update(unread=True)

    def serialize_latest_notifications(self, poll_viewers=None):
        """Returns a serialized version of the most recent unread elements in
        the queryset"""
        qs = self.unread()[:5]
        if poll_viewers:
            qs = qs.filter(poll_viewers=poll_viewers)[:5]

        notification_dic = serializers.serialize("json", qs)
        return notification_dic

    def get_most_recent(self, poll_viewers=None):
        """Returns the most recent unread elements in the queryset"""
        qs = self.unread()[:5]
        if poll_viewers:
            qs = qs.filter(poll_viewers=poll_viewers)[:5]

        return qs


class Notification(models.Model):
    

    creator = models.ForeignKey(User,
                              related_name="notify_actor",
                              on_delete=models.CASCADE)
    poll_viewers = models.ManyToManyField(User, blank=False,
                                  related_name="notifications")
    unread = models.BooleanField(default=True, db_index=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    verb = models.CharField(max_length=250, null=True, blank=True)
    #objects = NotificationQuerySet.as_manager()

    class Meta:
        verbose_name = _("Notification")
        verbose_name_plural = _("Notifications")
        ordering = ("-timestamp",)

    def __str__(self):
        pass
    

    def time_since(self, now=None):
        """
        Shortcut for the ``django.utils.timesince.timesince`` function of the
        current timestamp.
        """
        from django.utils.timesince import timesince

        return timesince(self.timestamp, now)

    def mark_as_read(self):
        if self.unread:
            self.unread = False
            self.save()

    def mark_as_unread(self):
        if not self.unread:
            self.unread = True
            self.save()

