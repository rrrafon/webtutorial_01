'''
This is where all the urls pertaining to MUSIC app should go
'''

from . import views
from django.http import HttpResponse
from django.urls import path, include

#This sets the namespace so when we call the url, we can use <namespace>:url link
# for example <a href="{% url 'music:musicDetails' album.id %}">
app_name = 'music'

urlpatterns = [
    #/music/
    path('', views.music_main, name = 'music'),
    # /music/<album_ID>
    path( '<album_ID>/', views.music_detail, name='musicDetails'),

    # /music/Favorite logic will perform tasks in the BG but will remain/reload the page
    path('<album_ID>/favorite/', views.music_favorite, name='musicFavorite'),

]