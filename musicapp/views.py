from django.shortcuts import render, get_object_or_404, redirect
from .models import Album
from .forms import AlbumForm


# Create your views here.
def index(request):
    albums = Album.objects.all()
    context = {
        'albums': albums
    }
    return render(request, 'musicapp/index.html', context)


def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    context = {
        'album': album
    }
    return render(request, 'musicapp/detail.html', context)


def create_album(request):
    form = AlbumForm(request.POST or None, request.FILES or None)     
    if form.is_valid:
        album = form.save(commit=False)
        album.cover = request.FILES['cover']
        album.save()
        return redirect('musicapp:index')
        
    return render(request, 'musicapp/add_album.html', {'form': form})