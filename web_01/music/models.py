from django.db import models
from django.urls import reverse

# Create your models here.
# each class creates a table and all variables correspond to a column

'''
    TO CREATE A SONG ON THE DATABASE: You may run python manage.py shell
    
    from music.models import Album, Song
    
    #this is a one way of assigning values
    album1 = Album()
    album1.artist = 'Parokya ni Edgar'
    album1.album_title = 'Bigotilyo' 
    album1.genre =  'OPM'
    album1.album_logo = 'place/Of/The/Logo.png' 
    
    # to create a song
    song = Song()
    song.album = album1 #since album is referenced/pointer
    song.file_type = 'mp3'
    song.song_title = 'Harana'
    # or create a song like this
    album1.song_set.create(song_title = 'Tsokolate', file_type = 'mp3') #automatically connected to album1
    album1.song_set.all() #list all song
    album1.song_set.count() #number of all song
    
'''


class Album(models.Model):
    artist = models.CharField(max_length= 150)
    album_title = models.CharField(max_length= 500)
    genre = models.CharField(max_length=150)
    #album_logo = models.CharField(max_length= 1000) #link to file
    album_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('music:musicDetails', kwargs= {'pk': self.pk})

    #returns a nice name when called
    def __str__(self):
        return '%s, %s' % (self.album_title, self.artist)


class Song(models.Model):
    #this name "album" is used in music_detail.html
    album = models.ForeignKey(Album,on_delete= models.CASCADE )
    file_type = models.CharField(max_length=20)
    song_title = models.CharField(max_length= 250)
    is_favorite =  models.BooleanField(default= False)

    def __str__(self):
        return self.song_title











