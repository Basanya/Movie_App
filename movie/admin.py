from django.contrib import admin
from .models import Movie
# Register your models here

class MovieAdmin(admin.ModelAdmin):
    list_display = ["title",'year_of_production','image']
    prepopulated_fields = {"slug":("title",)}

admin.site.register(Movie, MovieAdmin)

