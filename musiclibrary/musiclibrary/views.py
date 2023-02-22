from django.shortcuts import render
from django.http import HttpResponse
from song.models import Artist



def hello_world(request):
   return HttpResponse("Hello World!")

def home(request):
    return render(request,"home.html")

def artist(request):
    artist_list = Artist.objects.all()
    context = {'artist_list':artist_list}
    return render(request, 'artist.html', context)
