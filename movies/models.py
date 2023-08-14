from django.db import models

# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    birth_date = models.DateField()

    def __str__(self):
        return self.name
    

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

class Movie(models.Model):
    title = models.CharField(max_length=100)
    movie_id = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='movies/images/')
    director = models.ForeignKey(to=Director, on_delete=models.CASCADE)
    cast = models.TextField()
    genre = models.ManyToManyField(to=Genre)
    release_date = models.DateField()
    duration = models.IntegerField()
    trending = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

