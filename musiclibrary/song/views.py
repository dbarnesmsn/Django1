from django.shortcuts import render
from django.http import HttpResponse
from .models import Artist

'''
def artist(request):
    return HttpResponse("This is artist list")


def artist(request):
    artist_list = Artist.objects.all()
    context = {'artist_list':artist_list}
    return render(request, 'artist.html', context)
'''    