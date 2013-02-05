from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db import models

from django_extensions.db.models import TimeStampedModel
from django_countries.fields import CountryField

from clubmembers.clubs.models import Club, ClubRegion


class Member(TimeStampedModel):

    firstname = models.CharField(max_length=200,
        verbose_name=_('Firstname'))

    lastname = models.CharField(max_length=200,
        verbose_name=_('Lastname'))

    email = models.EmailField(blank=True, null=True,
        verbose_name=_('Email'))

    club_region = models.ForeignKey(ClubRegion,
        verbose_name=_("Region"))

    phonenumber = models.CharField(max_length=20,
        blank=True, null=True, verbose_name=_('Phonenumber'))

    address_street = models.CharField(max_length=100,
        blank=True, null=True, verbose_name=_("Street"))

    address_zip = models.CharField(max_length=20,
        blank=True, null=True, verbose_name=_("Zip"))

    address_state = models.CharField(max_length=50,
        blank=True, null=True, verbose_name=_("State"))

    country = CountryField(verbose_name=_('Country'))

    joined = models.DateField(verbose_name=_('Joined'))

    active = models.BooleanField(default=True,
        verbose_name=_('Active'))

    pdga_number = models.CharField(max_length=10,
        blank=True, null=True, verbose_name=_("PDGA Number"))

    added_by = models.ForeignKey(User,
        blank=True, null=True)

    birthdate = models.DateField(
        blank=True, null=True)

    class Meta:
        verbose_name = _('Member')
        verbose_name_plural = _('Members')

    def get_name(self):
        return '%s %s' % (self.firstname, self.lastname)

    def get_pdga_link(self):
        return 'http://www.pdga.com/player-stats?PDGANum=%s' % (self.pdga_number)

    def __unicode__(self):
        return '%s (ID: %i)' % (self.get_name(), self.id)


class MemberPayment(models.Model):
    member = models.ForeignKey(Member)
    club = models.ForeignKey(Club)
    added = models.DateTimeField()
    license_year = models.PositiveSmallIntegerField()
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=8)
