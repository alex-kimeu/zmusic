from django.db import models


# Tuple
GENRE = (
    ('unknown', 'UNKNOWN'), 
    ('hiphop', 'HIP HOP'),
    ('rhumba', 'RHUMBA'),
    ('trap', 'TRAP'),
    ('pop', 'POP'),
)

# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=25)
    artist = models.CharField(max_length=25)
    cover = models.ImageField()
    genre = models.CharField(max_length=25, choices=GENRE, default='Unknown')

    def __str__(self):
        return self.album_name
    


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=25)
    audio = models.FileField()
    lyrics = models.TextField()

    def __str__(self):
        return self.song_name
    
