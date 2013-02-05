from clubmembers.clubs.models import ClubAdmin

def club(request):
    context = {}

    if hasattr(request, 'club'):
        context.update({
            'club': request.club})

    if hasattr(request, 'is_club_admin'):
        context.update({
            'is_club_admin': request.is_club_admin})

    return context
