from . import views
from django.urls import path
from django.urls import include

app_name = 'movies'

urlpatterns = [
    path(route='', view=views.home, name='home'),
    path(route='search', view=views.search, name='search'),
    path(route='browse', view=views.browse, name='browse'),
    path(route='<int:id>/', view=views.detail, name='detail'),

]