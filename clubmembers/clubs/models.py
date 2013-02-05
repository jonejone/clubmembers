from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import User
from django.contrib.sites.models import Site


class Club(TimeStampedModel):
    name = models.CharField(max_length=100)

    yearly_fee = models.DecimalField(
        decimal_places=2,
        max_digits=8)

    yearly_fee_youth = models.DecimalField(
        decimal_places=2,
        max_digits=8)

    youth_age_limit = models.PositiveSmallIntegerField()

    currency = models.CharField(
        max_length=5, blank=True, null=True)

    payment_account_number = models.CharField(
        max_length=30, blank=True, null=True)

    def __unicode__(self):
        return self.name


class ClubSite(models.Model):
    club = models.ForeignKey(Club)
    site = models.ForeignKey(Site)


class ClubAdmin(models.Model):
    club = models.ForeignKey(Club)
    user = models.ForeignKey(User)


class ClubRegion(TimeStampedModel):
    name = models.CharField(max_length=100)
    club = models.ForeignKey(Club)

    def __unicode__(self):
        return self.name
