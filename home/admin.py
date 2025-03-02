from django.contrib import admin
from .models import Movie
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Movie)
class MovieAdmin(SummernoteModelAdmin):
    list_display = ('movie_title', 'slug', 'available')
    search_fields = ['movie_title']
    list_filter = ('available',)
    prepopulated_fields = {'slug': ('movie_title',)}
    summernote_fields = ('description',)

# Register your models here.
#admin.site.register(Movie)