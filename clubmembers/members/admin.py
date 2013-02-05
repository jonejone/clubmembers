from django.contrib import admin
from clubmembers.members.models import Member, MemberPayment


class MemberAdmin(admin.ModelAdmin):
    list_display = ('get_name', 'email', 'club_region',
        'added_by', 'phonenumber' )


class MemberPaymentAdmin(admin.ModelAdmin):
    list_display = ('member', 'license_year', 'club', 'amount')


admin.site.register(Member, MemberAdmin)
admin.site.register(MemberPayment, MemberPaymentAdmin)
