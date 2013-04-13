from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.forms.models import modelformset_factory
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404

from datetime import date

from clubmembers.clubs.models import Club
from clubmembers.members.models import Member
from clubmembers.members.forms import (RegisterMemberForm,
                                       MemberPaymentForm,)


@login_required
def account_profile(request):
    return render(
        request,
        'club/account/profile.html')


@login_required
def account_members(request):
    tmpl_dict = {
        'members': request.user.member_set.all(),
    }

    return render(
        request,
        'club/account/members.html',
        tmpl_dict)


def members(request):
    members = Member.objects.filter(
        club_region__club=request.club)

    data = {
        'members': members,
    }

    return render(request, 'club/members.html', data)


def index(request):
    return render(request, 'club/index.html')


def register(request):

    if request.method == 'POST':
        form = RegisterMemberForm(request.POST,
            request.FILES)
        if form.is_valid():
            new_member = form.save(commit=False)
            new_member.club = request.club

            if request.user.is_authenticated():
                new_member.added_by = request.user

            new_member.joined = date.today()
            new_member.save()
            return HttpResponseRedirect('/?saved=%i' % new_member.id)
    else:
        form = RegisterMemberForm()

    form.fields['club_region'].queryset = request.club.clubregion_set.all()
    form.fields['country'].initial = 'NO'

    data = {
        'form': form,
    }

    return render(request, 'club/register.html', data)


def member_edit(request, member_id):
    club = request.club

    if not request.is_club_admin:
        raise Http404

    try:
        member = Member.objects.filter(
            id=member_id, club_region__club=club)[0]
    except IndexError:
        raise Http404

    if request.method == 'POST':
        form = RegisterMemberForm(
            request.POST,
            instance=member,)

        if form.is_valid():
            new_member = form.save()
            return HttpResponseRedirect(reverse(
                'club-member', args=[new_member.id]))
    else:
        form = RegisterMemberForm(instance=member)

    form.fields['club_region'].queryset = request.club.clubregion_set.all()
    form.fields['joined'].initial = date.today()

    tmpl_dict = {
        'member': member,
        'form': form,
    }

    return render(request,
        'club/member/edit.html', tmpl_dict)


def member(request, member_id):
    club = request.club

    try:
        member = Member.objects.filter(
            id=member_id, club_region__club=club)[0]
    except IndexError:
        raise Http404

    if request.method == 'POST':
        payment_form = MemberPaymentForm(request.POST,
            member=member)

        if payment_form.is_valid():
            payment = payment_form.save()
            return HttpResponseRedirect(
                '%s?payment_saved=1' % reverse(
                    'club-member', args=[member.id, ]))
    else:
        payment_form = MemberPaymentForm(
            member=member)

    data = {
        'member': member,
        'payment_form': payment_form,
    }

    return render(request, 'club/member.html', data)
