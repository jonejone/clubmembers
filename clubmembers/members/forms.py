from django.forms import ModelForm
from django.forms.models import modelformset_factory
from clubmembers.members.models import Member


class RegisterMemberForm(ModelForm):
    class Meta:
        model = Member
        exclude = ('club',)
