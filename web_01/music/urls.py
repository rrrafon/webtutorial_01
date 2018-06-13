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
    path('', views.IndexView.as_view() , name = 'music'),
    # /music/register/  --> registers new user
    path( 'register/', views.UserFormView.as_view() , name='musicRegister'),
    # /music/<album_ID>
    path( '<pk>/', views.DetailView.as_view() , name='musicDetails'),
    # /music/album/add/
    path( 'album/add/', views.AlbumCreate.as_view() , name='musicCreateAlbum'),
    # /music/album/<album id>/
    path( 'album/<pk>/', views.AlbumEdit.as_view() , name='musicEditAlbum'),
    # /music/album/<album id>/delete/
    path( 'album/<pk>/delete/', views.AlbumDelete.as_view() , name='musicDeleteAlbum'),

]