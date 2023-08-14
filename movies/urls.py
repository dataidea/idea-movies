from . import views
from django.urls import path
from django.urls import include

app_name = 'movies'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:movie_id>/', views.detail, name='detail'),

]