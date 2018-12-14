# from django.db import models
# from polls.models import Poll, Choices
# from django.contrib.auth.models import User
#
#
# # Create your models here.
# class Vote(models.Model):
#     choice = models.ForeignKey(Choices, related_name='votes', on_delete=models.CASCADE)
#     poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
#     voted_by = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     class Meta:
#         unique_together = ("poll", "voted_by")