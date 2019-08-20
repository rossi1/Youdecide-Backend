import uuid
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core import serializers
from django.db import models
from django.utils.translation import ugettext_lazy as _
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
    poll_viewers = models.ForeignKey(User, blank=False,
                                  related_name="notifications", on_delete=models.CASCADE)
    unread = models.BooleanField(default=True, db_index=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    uuid_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=210, null=True, blank=True)
    verb = models.CharField(max_length=1)
    action_object_content_type = models.ForeignKey(ContentType,
                                                   blank=True, null=True, related_name="notify_action_object",
                                                   on_delete=models.CASCADE)
    action_object_object_id = models.CharField(
        max_length=50, blank=True, null=True)
    action_object = GenericForeignKey(
        "action_object_content_type", "action_object_object_id")
    objects = NotificationQuerySet.as_manager()

    class Meta:
        verbose_name = _("Notification")
        verbose_name_plural = _("Notifications")
        ordering = ("-timestamp",)

    def __str__(self):
        if self.action_object:
            return '{} {} {self.action_object} {} ago'.format(self.actor,self.get_verb_display(), self.time_since())

        return '{} {} {} ago'.format(self.actor, self.get_verb_display(), self.time_since())
    """
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify('{} {} {}'.format(self.poll_viewers,self.uuid_id, self.verb ),
                                to_lower=True, max_length=200)

        super().save(*args, **kwargs)
    """

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


def notification_handler(actor, poll_viewers, verb, **kwargs):
    """
    Handler function to create a Notification instance.
    :requires:
    :param actor: User instance of that user who makes the action.
    :param poll_viewers: User instance, a list of User instances or string
                      'global' defining who should be notified.
    :param verb: Notification attribute with the right choice from the list.

    :optional:
    :param action_object: Model instance on which the verb was executed.
    :param key: String defining what kind of notification is going to be created.
    :param id_value: UUID value assigned to a specific element in the DOM.
    """
    key = kwargs.pop('key', 'notification')
    id_value = kwargs.pop('id_value', None)
    if poll_viewers == 'global':
        users = get_user_model().objects.all().exclude(username=actor.username)
        for user in users:
            Notification.objects.create(
                actor=actor,
                poll_viewers=user,
                verb=verb,
                action_object=kwargs.pop('action_object', None)
            )
        notification_broadcast(actor, key)

    elif isinstance(poll_viewers, list):
        for user in poll_viewers:
            Notification.objects.create(
                actor=actor,
                poll_viewers=get_user_model().objects.get(username=user),
                verb=verb,
                action_object=kwargs.pop('action_object', None)
            )

    elif isinstance(poll_viewers, get_user_model()):
        Notification.objects.create(
            actor=actor,
            poll_viewers=poll_viewers,
            verb=verb,
            action_object=kwargs.pop('action_object', None)
        )
        notification_broadcast(
            actor, key, id_value=id_value, poll_viewers=poll_viewers.username)

    else:
        pass


def notification_broadcast(actor, key, **kwargs):
    """Notification handler to broadcast calls to the recieve layer of the
    WebSocket consumer of this app.
    :requires:
    :param actor: User instance of that user who makes the action.
    :param key: String parameter to indicate the client which action to
                perform.

    :optional:
    :param id_value: UUID value assigned to a specific element in the DOM.
    :param poll_viewers: String indicating the name of that who needs to be
                      notified.
    """
    """
    channel_layer = get_channel_layer()
    id_value = kwargs.pop('id_value', None)
    poll_viewers = kwargs.pop('poll_viewers', None)
    payload = {
            'type': 'receive',
            'key': key,
            'actor_name': actor.username,
            'id_value': id_value,
            'poll_viewers': poll_viewers
        }
    async_to_sync(channel_layer.group_send)('notifications', payload)
    """
