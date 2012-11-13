from django.shortcuts import render
from clubmembers.clubs.models import Club

def index(request):
    clubs = Club.objects.all()

    return render(request, 'index.html', {
        'clubs': clubs})


def register(request):
    data = {

    }
    
    return render(request, 'register.html', data)
