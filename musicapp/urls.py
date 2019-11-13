from django.urls import path
from . import views

app_name = 'musicapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('(?P<album_id>[0-9]+)/', views.detail, name='detail'),
    path('add-album', views.add_album, name='add-album'),
    path('(?P<album_id>[0-9]+)/update-album', views.update_album, name='update-album'),
]