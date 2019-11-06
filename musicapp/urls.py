from django.urls import path
from . import views

app_name = 'musicapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('(?P<album_id>[0-9]+)/', views.detail, name='detail'),
    path('add-album', views.create_album, name='add-album'),
]