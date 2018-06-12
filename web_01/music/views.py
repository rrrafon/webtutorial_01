#to use templates import this, this is thhe shortcut command
from django.shortcuts import render, get_object_or_404

#import database commands, '.' dot represents in this folder
from .models import Album, Song



def music_main(request):
    pageTitle = 'Albums'
    all_albums = Album.objects.all()
    #should be dictionary, this is where you put variables
    context = {
        'var_all_albums': all_albums,
        'var_page_title': pageTitle,
        }
    #this code automatically look inside the templates folder
    return render(request, 'music/music_main.html', context)

def music_detail(request, album_ID):
    #gets the object or return 404 if not found
    album = get_object_or_404(Album, pk = album_ID)

    context = {
        'var_page_title': album.artist,
        'var_album': album,
        'var_songs': album.song_set.all()
        }
    return render(request, 'music/music_detail.html', context)

def music_favorite(request, album_ID):
    #gets the object or return 404 if not found
    album = get_object_or_404(Album, pk = album_ID)

    #Query database
    try:
        selected_song = album.song_set.get(pk = request.POST["val_song"])

    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/music_detail.html', {
        'var_album': album,
        'var_songs': album.song_set.all(),
        'var_errorMsg': "You did not select a valid song",
        })

    else:

        if selected_song.is_favorite == True:
            selected_song.is_favorite = False
        else:
            selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/music_detail.html', {
        'var_album': album,
        'var_songs': album.song_set.all(),
        })

