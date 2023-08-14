from django.db.models import Q
from movies.models import Movie
from django.shortcuts import render

# Create your views here.
def home(request):
    trending = Movie.objects.filter(trending=True)
    movies = Movie.objects.all()
    context = {
        'trending': trending,
        'movies': movies
    }
    template_name = 'movies/home.html'
    return render(request=request, template_name=template_name, context=context)

def detail(request, movie_id):
    return render(request, 'movies/detail.html')

def movies(request):
    return render(request, 'movies/movies.html')

def search(request):
    query = request.GET.get('q')
    if query:
        movies = Movie.objects.filter(Q(title__icontains=query) | Q(overview__icontains=query))
    else:
        movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/search.html', context)