from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    artist = models.CharField(max_length=100)
    mp3_file = models.FileField(upload_to='mp3_files')
    text = models.TextField(blank=True)
    release_date = models.DateField()
    album = models.ForeignKey('Album', on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(upload_to = 'static/songs_of_SS/media', null=True)

    def __str__(self):
        return self.title
    

class Album(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    release_date = models.DateField()
    number_of_songs = models.IntegerField()
    photo = models.ImageField(upload_to = 'static/songs_of_SS/media', null=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.name
    
class Video(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    mp4_file = models.FileField(upload_to='mp4_files')
    song = models.ForeignKey('Song', on_delete=models.SET_NULL, null=True)








# user
# mko0nji9
