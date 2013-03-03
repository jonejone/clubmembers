from django.conf import settings
from django.contrib.sites.models import get_current_site
from clubmembers.clubs.models import Club, ClubAdmin

class ClubMiddleware:
    def process_request(self, request):
        site = get_current_site(request)

        if site.clubsite_set.count():
            request.club = site.clubsite_set.all()[0].club
            request.urlconf = 'clubmembers.clubs.urls'

            admin = False
            if request.user.is_authenticated():
                try:
                    clubadmin = request.user.clubadmin_set.get(
                        club=request.club)
                except ClubAdmin.DoesNotExist:
                    pass
                else:
                    admin = True

                if request.user.is_staff or request.user.is_superuser:
                    admin = True

            request.is_club_admin = admin

        return None
