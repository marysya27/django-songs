from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('show_songs', views.ShowSongs.as_view(), name='show_songs'),
    path('show_albums', views.ShowAlbums.as_view(), name='show_albums'),
    path('<slug:slug>/sdescription', views.SongDescription.as_view(), name='song_description'),
    path('<slug:slug>/adescription', views.AlbumDescription.as_view(), name='album_description'),
    path('register', views.RegisterUser.as_view(), name='register'),
    path('login', views.LoginUser.as_view(), name='login'),
    path('logout', views.logout_user, name='logout'),
    path('about', views.about, name='about'),
    path('video', views.ShowVideo.as_view(), name='video'),
    path('search', views.Search.as_view(), name='search'),
]

