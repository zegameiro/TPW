from datetime import datetime
from io import StringIO

from django.core.handlers.wsgi import WSGIRequest

import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Album, Music, Artist, Playlist, Membership, Performer, Band, Genre, Listener
from django.contrib.auth import views as auth_views
from MusicPlayer.forms import LoginForm, SignUpForm, MusicSearchForm, AddEditArtistForm, AddEditMusicForm, \
    AddEditBandForm, \
    AddEditAlbumForm, AddEditPlaylistForm, AddEditGenreForm
from django.contrib.auth import login
from django.db.models import Q, Case, When, Value, BooleanField, ProtectedError
from itertools import groupby
from django.http import JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import IntegrityError
from django.utils.translation import gettext_lazy as _
### Web Services 2nd Project
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from MusicPlayer.serializers import MusicSerializer, GenreSerializer, AlbumSerializer, ArtistSerializer, BandSerializer, \
    PerformerSerializer, \
    ListenerSerializer, UserSerializer, PlaylistSerializer, MembershipSerializer
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.exceptions import TokenError


### Web Services 2nd Project
"""
In auth_sign_in and auth_sign_up I send the access token in response and the refresh token in an httponly cookie
In the frontend will only work with the access token which will be saved in the local storage (and not with the
refresh token as it is httponly)
https://www.cyberchief.ai/2023/05/secure-jwt-token-storage.html
"""

@api_view(['POST'])
def auth_sign_in(request):
    serializer = TokenObtainPairSerializer(data=request.data, context={'request': request})
    serializer.is_valid(raise_exception=True)
    access = AccessToken(serializer.validated_data['access'])
    access.payload["is_superuser"] = serializer.user.is_superuser
    refresh = serializer.validated_data['refresh']
    response = Response({
        "access": str(access)
    })
    response.set_cookie(key='refresh', value=refresh, httponly=True, samesite='None', secure=True)
    return response


@api_view(['POST'])
def auth_sign_up(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user=user)
        access = refresh.access_token
        # user.is_superuser dar sempre false portanto mais vale pôr false
        access.payload["is_superuser"] = False
        response = Response({
            "access": str(access)
        }, status=status.HTTP_201_CREATED)
        response.set_cookie(key='refresh', value=refresh, httponly=True, samesite='None', secure=True)
        return response
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def auth_refresh(request):
    if 'refresh' not in request.COOKIES:
        return Response({"error": "refresh token expired or it doesn't exist"}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        refresh = RefreshToken(request.COOKIES["refresh"])
        user = Listener.objects.get(id=refresh.payload["user_id"])
        new_access = refresh.access_token
        new_access.payload["is_superuser"] = user.is_superuser
        response = Response({
            "access": str(new_access)
        })
        response.set_cookie(key='refresh', value=refresh, httponly=True, samesite='None', secure=True)
        print(new_access)
        print(refresh)
    except TokenError:
        response = Response({"error": "refresh token expired or it doesn't exist"}, status=status.HTTP_401_UNAUTHORIZED)
    return response


@api_view(['GET'])
def get_musics_by_genre(request):
    musics = Music.objects.all()
    serialized_data = {genre: MusicSerializer(musics, many=True).data for genre, musics in
                       groupby(sorted(musics, key=lambda music: music.genre.title.upper()),
                               key=lambda music: music.genre.title.upper())}
    return Response(serialized_data)


@api_view(['GET'])
def get_musics(request):
    musics = Music.objects.all()
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_genres(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_albums(request):
    albums = Album.objects.all()
    serializer = AlbumSerializer(albums, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_artists(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_bands(request):
    bands = Band.objects.all()
    serializer = BandSerializer(bands, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_artist(request, id):
    try:
        artist = Artist.objects.get(id=id)
    except Artist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ArtistSerializer(artist)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def add_artist(request):
    serializer = ArtistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def delete_artist(request, id):
    try:
        artist = Artist.objects.get(id=id)
    except Artist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    artist.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsAdminUser])
def update_artist(request, id):
    try:
        artist = Artist.objects.get(id=id)
    except Artist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    request.data._mutable = True
    if request.data.get('image') == '':
        request.data['image'] = artist.image
    request.data._mutable = False
    serializer = ArtistSerializer(artist, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_genre(request, id):
    try:
        genre = Genre.objects.get(id=id)
    except Genre.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = GenreSerializer(genre)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def add_genre(request):
    serializer = GenreSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def delete_genre(request, id):
    try:
        genre = Genre.objects.get(id=id)
    except Genre.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    genre.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsAdminUser])
def update_genre(request, id):
    try:
        genre = Genre.objects.get(id=id)
    except Genre.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    request.data._mutable = True
    if request.data.get('image') == '':
        request.data['image'] = genre.image
    request.data._mutable = False
    serializer = GenreSerializer(genre, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_band(request, id):
    try:
        band = Band.objects.get(id=id)
    except Band.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = BandSerializer(band)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def add_band(request):
    serializer = BandSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def delete_band(request, id):
    try:
        band = Band.objects.get(id=id)
    except Band.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    band.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsAdminUser])
def update_band(request, id):
    try:
        band = Band.objects.get(id=id)
    except Band.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    request.data._mutable = True
    if request.data.get('image') == '':
        request.data['image'] = band.image
    request.data._mutable = False
    serializer = BandSerializer(band, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_album(request, id):
    try:
        album = Album.objects.get(id=id)
    except Album.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = AlbumSerializer(album)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def add_album(request):
    serializer = AlbumSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def delete_album(request, id):
    try:
        album = Album.objects.get(id=id)
    except Album.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    album.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsAdminUser])
def update_album(request, id):
    try:
        album = Album.objects.get(id=id)
    except Album.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    request.data._mutable = True
    if request.data.get('image') == '':
        request.data['image'] = album.image
    request.data._mutable = False
    serializer = AlbumSerializer(album, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_music(request, id):
    try:
        music = Music.objects.get(id=id)
    except Music.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = MusicSerializer(music)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def add_music(request):
    serializer = MusicSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def delete_music(request, id):
    try:
        music = Music.objects.get(id=id)
    except Music.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    music.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsAdminUser])
def update_music(request, id):
    try:
        music = Music.objects.get(id=id)
    except Music.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    request.data._mutable = True
    if request.data.get('image') == '':
        request.data['image'] = music.image
    if request.data.get('audio_file') == '':
        request.data['audio_file'] = music.audio_file
    request.data._mutable = False
    serializer = MusicSerializer(music, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_performers(request):
    performers = Performer.objects.all()
    serializer = PerformerSerializer(performers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def search_music(request):
    query = request.query_params.get('query', default=None)

    if query is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    songs = Music.objects.filter(
        Q(name__icontains=query) | Q(performer__name__icontains=query) | Q(genre__title__icontains=query) | Q(
            album__name__icontains=query)
    )

    serializer = {genre: MusicSerializer(musics, many=True).data for genre, musics in
                  groupby(sorted(songs, key=lambda music: music.genre.title.upper()),
                          key=lambda music: music.genre.title.upper())}

    return Response(serializer)


@api_view(['GET'])
def get_albums_by_performer(request, id):
    if id is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    albums = Album.objects.filter(performer__id=id)
    serializer = AlbumSerializer(albums, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def get_musics_by_artist(request, id):
    if id is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    musics = Music.objects.filter(performer__id=id)
    serializer = MusicSerializer(musics, many=True)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_playlists(request):
    print("GETTING PLAYLISTS: ", Playlist.objects.filter(author=request.user))
    serializer = PlaylistSerializer(Playlist.objects.filter(author=request.user), many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_playlist(request, id):
    try:
        playlist = Playlist.objects.get(author=request.user, id=id)
    except Playlist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PlaylistSerializer(playlist)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_playlist(request):
    request.data["author"] = request.user.pk
    serializer = PlaylistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_playlist(request, playlist_id):
    try:
        playlist = Playlist.objects.get(author=request.user, id=playlist_id)
    except Playlist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    playlist.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_music_to_playlist(request, songId, playlistId):
    try:
        song = Music.objects.get(id=songId)
        playlist = Playlist.objects.get(author=request.user, id=playlistId)
    except (Music.DoesNotExist, Playlist.DoesNotExist):
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = MembershipSerializer(data={'playlist': playlistId, 'music': songId})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_song_playlist(request, songId, playlistId):
    try:
        membership = Membership.objects.get(playlist=playlistId, music=songId)
        if membership.playlist.author != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    except Membership.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    membership.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def sort_playlist(request, playlistId, prevPosition, nextPosition):
    try:
        playlist = Playlist.objects.get(author=request.user, id=playlistId)
    except Playlist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    playlist.change_order(prevPosition, nextPosition)
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_performer_information(request, performerId):
    try:
        artist_details = Artist.objects.get(id=performerId)
        serializer = ArtistSerializer(artist_details)
    except Artist.DoesNotExist:
        artist_details = Band.objects.get(id=performerId)
        serializer = BandSerializer(artist_details)

    return Response(serializer.data)


@api_view(['GET'])
def get_musics_by_album(request, albumId):
    try:
        musics = Music.objects.filter(album=albumId)
    except Music.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_like(request, songId):
    try:
        music = Music.objects.get(id=songId)
        music.likes.add(request.user)
        return Response(status=status.HTTP_201_CREATED)
    except Music.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_like(request, songId):
    try:
        music = Music.objects.get(id=songId)
        music.likes.remove(request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Music.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

