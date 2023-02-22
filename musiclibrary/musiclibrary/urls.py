from django.contrib import admin
from django.urls import path
from . import views
#from song.views import artist

urlpatterns = [
    path('say-hello/', views.hello_world),
    path('', views.home),
    path('admin/', admin.site.urls),
    path('artist/', views.artist)
]
