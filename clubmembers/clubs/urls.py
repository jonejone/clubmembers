from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('clubmembers.frontend.club_views',
    url(r'^$', 'index', name='club-index'),
    url(r'^register/$', 'register', name='club-register'),
    url(r'^members/$', 'members', name='club-members'),
    url(r'^members/(?P<member_id>\d+)/$', 'member', name='club-member'),
    url(r'^members/(?P<member_id>\d+)/edit/$', 'member_edit', name='club-member-edit'),

    url(r'^accounts/members/', 'account_members', name='club-account-members'),
    url(r'^accounts/profile/', 'account_profile', name='club-account-profile'),
    url(r'^accounts/', include('clubmembers.frontend.registration_urls')),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
