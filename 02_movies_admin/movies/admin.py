from django.contrib import admin

# Register your models here.

from .models.genre import Genre
from .models.genre_filmwork import GenreFilmwork
from .models.filmwork import Filmwork
from .models.person import Person
from .models.person_filmwork import PersonFilmWork


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    # Отображение полей в списке
    list_display = ('name', 'description',)
    # Поиск по полям
    search_fields = ('name', 'description', 'id',)


class PersonFilmworkInline(admin.TabularInline):
    model = PersonFilmWork
    autocomplete_fields = ('person',)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):

    list_display = ('full_name',)
    search_fields = ('full_name',)


class GenreFilmworkInline(admin.TabularInline):
    model = GenreFilmwork


@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    inlines = (GenreFilmworkInline, PersonFilmworkInline,)

    # Отображение полей в списке
    list_display = ('title', 'type', 'creation_date', 'rating',)
    # Фильтрация в списке
    list_filter = ('type', 'rating',)
    # Поиск по полям
    search_fields = ('title', 'description', 'id',)
