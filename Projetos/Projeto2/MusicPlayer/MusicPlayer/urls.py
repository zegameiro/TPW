"""MusicPlayer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from MusicPlayer import views
from MusicPlayer.forms import LoginForm, SignUpForm
from django.contrib.auth import views as auth_views
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    ### Web Services 2nd Project
    path('ws/auth/sign-in', views.auth_sign_in),
    path('ws/auth/sign-up', views.auth_sign_up),
    path('ws/auth/refresh', views.auth_refresh),
    path('ws/musicsbygenre', views.get_musics_by_genre),
    path('ws/musics', views.get_musics),
    path('ws/genres', views.get_genres),
    path('ws/albums', views.get_albums),
    path('ws/artists', views.get_artists),
    path('ws/bands', views.get_bands),
    path('ws/addArtist', views.add_artist),
    path('ws/artist/<int:id>', views.get_artist),
    path('ws/updateArtist/<int:id>', views.update_artist),
    path('ws/deleteArtist/<int:id>', views.delete_artist),
    path('ws/addGenre', views.add_genre),
    path('ws/genre/<int:id>', views.get_genre),
    path('ws/updateGenre/<int:id>', views.update_genre),
    path('ws/deleteGenre/<int:id>', views.delete_genre),
    path('ws/addBand', views.add_band),
    path('ws/band/<int:id>', views.get_band),
    path('ws/updateBand/<int:id>', views.update_band),
    path('ws/deleteBand/<int:id>', views.delete_band),
    path('ws/addAlbum', views.add_album),
    path('ws/album/<int:id>', views.get_album),
    path('ws/updateAlbum/<int:id>', views.update_album),
    path('ws/deleteAlbum/<int:id>', views.delete_album),
    path('ws/addMusic', views.add_music),
    path('ws/music/<int:id>', views.get_music),
    path('ws/updateMusic/<int:id>', views.update_music),
    path('ws/deleteMusic/<int:id>', views.delete_music),
    path('ws/performers', views.get_performers),
    path('ws/searchMusic', views.search_music),
    path('ws/getAlbumsByPerformer/<int:id>', views.get_albums_by_performer),
    path('ws/getMusicsByPerformer/<int:id>', views.get_musics_by_artist),
    path('ws/getPerformerDetails/<int:performerId>', views.get_performer_information),
    path('ws/getMusicsByAlbum/<int:albumId>', views.get_musics_by_album),
    path('ws/playlist/<int:id>', views.get_playlist),
    path('ws/playlists', views.get_playlists),
    path('ws/addPlaylist', views.add_playlist),
    path('ws/deletePlaylist/<int:playlist_id>', views.delete_playlist),
    path('ws/addMusicToPlaylist/<int:songId>/<int:playlistId>', views.add_music_to_playlist),
    path('ws/deleteSongPlaylist/<int:songId>/<int:playlistId>', views.delete_song_playlist),
    path('ws/addLike/<int:songId>', views.add_like),
    path('ws/removeLike/<int:songId>', views.remove_like),
    path('ws/sortPlaylist/<int:playlistId>/<int:prevPosition>/<int:nextPosition>', views.sort_playlist),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
