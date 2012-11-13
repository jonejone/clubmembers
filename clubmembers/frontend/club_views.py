from django.shortcuts import render
from django.conf import settings
from django.forms.models import modelformset_factory
from django.http import HttpResponse, HttpResponseRedirect, Http404

from datetime import date

from clubmembers.clubs.models import Club
from clubmembers.members.models import Member
from clubmembers.members.forms import RegisterMemberForm

def index(request):
    club = Club.objects.get(id=settings.CLUB_ID)
    members = Member.objects.filter(
        club_region__club=club)

    data = {
        'club': club,
        'members': members,
    }

    return render(request, 'club/index.html', data)


def register(request):
    club = Club.objects.get(id=settings.CLUB_ID)

    if request.method == 'POST':
        form = RegisterMemberForm(request.POST,
            request.FILES)
        if form.is_valid():
            new_member = form.save(commit=False)
            new_member.club = club
            new_member.save()
            return HttpResponseRedirect('/?saved=%i' % new_member.id)
    else:
        form = RegisterMemberForm()

    form.fields['club_region'].queryset = club.clubregion_set.all()
    form.fields['joined'].initial = date.today()

    data = {
        'club': club,
        'form': form,
    }

    return render(request, 'club/register.html', data)


def member(request, member_id):
    club = Club.objects.get(id=settings.CLUB_ID)

    try:
        member = Member.objects.filter(
            id=member_id, club_region__club=club)[0]
    except IndexError:
        raise Http404

    data = {
        'member': member,
        'club': club,
    }

    return render(request, 'club/member.html', data)
