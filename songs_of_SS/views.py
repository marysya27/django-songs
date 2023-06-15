from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import redirect


from .models import *
from .utils import *
from .forms import *


class HomePageView(DataMixin, TemplateView):
    template_name = 'songs_of_SS/index.html'

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title = 'База')
        return dict(list(context.items())+list(context_def.items()))


class ShowSongs(DataMixin, ListView):
    paginate_by = 7
    model = Song
    template_name = 'songs_of_SS/show_songs.html'
    context_object_name = 'songs'

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title = 'Пісеньки')
        return dict(list(context.items())+list(context_def.items()))
    
    def get_ordering(self):
        return ['-release_date']
    

class Search(DataMixin, ListView):
    template_name = 'songs_of_SS/show_songs.html'
    context_object_name = 'songs'

    def get_queryset(self):
        return Song.objects.filter(title__iregex=self.request.GET.get('q'))
    
    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title = 'Пісеньки', q =self.request.GET.get('q'))
        return dict(list(context.items())+list(context_def.items()))
    

class SongDescription(DataMixin, DetailView):
    model = Song
    template_name = 'songs_of_SS/song_description.html'
    context_object_name = 'song'

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title = context['song'])
        return dict(list(context.items())+list(context_def.items()))


class AlbumDescription(DataMixin, DetailView):
    model = Album
    template_name = 'songs_of_SS/album_description.html'
    context_object_name = 'album'
    
    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        a = Album.objects.filter(name = context['album'])
        context_def = self.get_user_context(title = context['album'], songs = Song.objects.filter(album = a[0].pk))
        return dict(list(context.items())+list(context_def.items()))


class ShowAlbums(DataMixin, ListView):
    model = Album
    template_name = 'songs_of_SS/show_albums.html'
    context_object_name = 'albums'

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title = 'Альбоми')
        return dict(list(context.items())+list(context_def.items()))
    
def about(request):
    return render(request, 'songs_of_SS/about.html', {'header_links' : header_links})

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'songs_of_SS/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title = 'Реєстрація')
        return dict(list(context.items())+list(context_def.items()))
    
class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'songs_of_SS/login.html'

    def get_context_data(self, *, objects_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title = 'Авторизація')
        return dict(list(context.items())+list(context_def.items()))
    
    def get_success_url(self):
        return reverse_lazy('home')
    
def logout_user(request):
    logout(request)
    return redirect('login')


def print(request):
    return HttpResponse('<h1>mldmbkxcx</h1>')

class ShowVideo(DataMixin, ListView):
    model = Video
    template_name = 'songs_of_SS/show_video.html'
    context_object_name = 'video'

    def get_context_data(self, *, objects_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title = 'Відосики')
        return dict(list(context.items())+list(context_def.items()))




# def showvideo(request):
#     vid = Video.objects.get(pk=1)
#     return render(request, 'songs_of_SS/show_video.html', {'title' : 'video', 'vid' : vid})