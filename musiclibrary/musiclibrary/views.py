from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required 
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

#def signup(request):
#    return render(request, 'signup.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

'''
def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('home')  
        
    else:
        form = AuthenticationForm()
    return render(request,'signin.html', {"form":form})
'''
def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in user
            user = form.get_user() 
            login(request,user)
        return redirect('home')  
    else:
        form = AuthenticationForm()
    return render(request,'signin.html', {"form":form})
