from django.forms import ModelForm
from clubmembers.members.models import Member, MemberPayment
from datetime import datetime


class EditMemberForm(ModelForm):
    class Meta:
        model = Member
        exclude = ('club', 'added_by')


class RegisterMemberForm(ModelForm):
    class Meta:
        model = Member
        exclude = ('club', 'added_by', 'active', 'joined')


class MemberPaymentForm(ModelForm):
    class Meta:
        model = MemberPayment
        fields = ('license_year', 'amount')

    def __init__(self, *kargs, **kwargs):
        if not 'member' in kwargs:
            raise Exception('MemberPaymentForm requires member')

        self.member = kwargs.get('member')
        del kwargs['member']

        super(MemberPaymentForm, self).__init__(
            *kargs, **kwargs)

    def save(self, *kargs, **kwargs):
        kwargs['commit'] = False
        payment = super(MemberPaymentForm, self).save(
            *kargs, **kwargs)

        payment.added = datetime.now()
        payment.club = self.member.club_region.club
        payment.member = self.member

        payment.save()
        return payment
