from django.contrib import admin
from django.urls import path
from . import views
#from song.views import artist
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


urlpatterns = [
    path('say-hello/', views.hello_world),
    path('', views.home, name="home"),
    path('admin/', admin.site.urls),
    path('artist/', views.artist),
    path('signup/', views.signup),
    path('home/', views.home, name="home"),
    path('signin/', views.signin, name="signin"),
]

urlpatterns+=staticfiles_urlpatterns()
