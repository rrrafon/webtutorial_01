from django.contrib import admin
from .models import Album, Song
# Register your models here.

#to register table on admin page so you can edit it
#execute these commands

admin.site.register(Album)
admin.site.register(Song)



