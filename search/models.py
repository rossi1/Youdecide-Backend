from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    search = models.CharField(max_length=255)
    search_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.search

    class Meta:
        verbose_name_plural = 'Search Histories'
