from django.contrib import admin
from .models import *

class SongAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

class AlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class VidoeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    
    def save_model(self, request, obj, form, change):
        obj.slug = 'video-' + obj.slug
        super().save_model(request, obj, form, change)


admin.site.register(Song, SongAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Video, VidoeAdmin)
