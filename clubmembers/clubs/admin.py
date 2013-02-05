from django.contrib import admin
from clubmembers.clubs.models import (  Club,
                                        ClubRegion,
                                        ClubSite,
                                        ClubAdmin)


class ClubSiteAdmin(admin.ModelAdmin):
    list_display = ('club', 'site')


class ClubAdminAdmin(admin.ModelAdmin):
    list_display = ('club', 'user')


admin.site.register(Club)
admin.site.register(ClubRegion)
admin.site.register(ClubSite, ClubSiteAdmin)
admin.site.register(ClubAdmin, ClubAdminAdmin)
