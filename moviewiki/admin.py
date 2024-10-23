from django.contrib import admin
from moviewiki.models import(
    Movie,
    Genre,
    Poster
)

class AdminTable(admin.ModelAdmin):
    list_display = ['title', 'overview', 'release_date']

admin.site.register(Movie, AdminTable)
admin.site.register([Genre, Poster])
