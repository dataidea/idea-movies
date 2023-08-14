from django import forms
from .models import Genre
from .models import Movie
from .models import Director
from django.db import models
from django.contrib import admin

class MovieAdmin(admin.ModelAdmin):
    filter_horizontal = ('genre',)

# Register your models here.
# admin.site.register(model_or_iterable=models.User)
admin.site.register(model_or_iterable=Movie, admin_class=MovieAdmin)
admin.site.register(model_or_iterable=Director)
admin.site.register(model_or_iterable=Genre)

# django admin customization
admin.site.site_header = 'IDEA MOVIE ADMIN'
admin.site.index_title = 'Admin'