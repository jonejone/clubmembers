from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('clubmembers.frontend.club_views',
    url(r'^$', 'index', name='club-index'),
    url(r'^register/$', 'register', name='club-register'),
    url(r'^member/(?P<member_id>\d)/$', 'member', name='club-member'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
