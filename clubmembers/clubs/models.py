from django.db import models
from django_extensions.db.models import TimeStampedModel


class Club(TimeStampedModel):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name



class ClubRegion(TimeStampedModel):
    name = models.CharField(max_length=100)
    club = models.ForeignKey(Club)

    def __unicode__(self):
        return self.name
